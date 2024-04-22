import time
import RPi.GPIO as GPIO
import smbus
from mpu6050 import mpu6050

sensor_left = mpu6050(0x68)
sensor_right = mpu6050(0x69)

motor_left_pin1 = 17
motor_left_pin2 = 18
motor_right_pin1 = 23
motor_right_pin2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_left_pin1, GPIO.OUT)
GPIO.setup(motor_left_pin2, GPIO.OUT)
GPIO.setup(motor_right_pin1, GPIO.OUT)
GPIO.setup(motor_right_pin2, GPIO.OUT)

motor_left_pwm = GPIO.PWM(motor_left_pin1, 1000)
motor_right_pwm = GPIO.PWM(motor_right_pin1, 1000)

motor_left_pwm.start(0)
motor_right_pwm.start(0)

Kp = 1.0
Ki = 0.1
Kd = 0.01

error_prev = 0
integral = 0

UMBRAL_MOVIMIENTO = 1.0

bus = smbus.SMBus(1)

def pid_control(error):
    global integral, error_prev
    integral += error
    derivative = error - error_prev
    output = Kp * error + Ki * integral + Kd * derivative
    error_prev = error
    return output

def control_motors(control_signal):
    if control_signal > 0:
        motor_left_pwm.ChangeDutyCycle(control_signal)
        motor_right_pwm.ChangeDutyCycle(0)
        GPIO.output(motor_left_pin2, GPIO.LOW)
        GPIO.output(motor_right_pin2, GPIO.LOW)
    else:
        motor_left_pwm.ChangeDutyCycle(0)
        motor_right_pwm.ChangeDutyCycle(-control_signal)
        GPIO.output(motor_left_pin2, GPIO.LOW)
        GPIO.output(motor_right_pin2, GPIO.LOW)

def detect_arm_movement(inclination_left, inclination_right):
    if inclination_left > inclination_right:
        return 1
    elif inclination_left < inclination_right:
        return 2
    else:
        return 0

while True:
    gyro_left = sensor_left.get_gyro_data()
    gyro_right = sensor_right.get_gyro_data()

    inclination_left = gyro_left['z']
    inclination_right = gyro_right['z']

    error = inclination_left - inclination_right

    arm_movement = detect_arm_movement(inclination_left, inclination_right)

    bus.write_byte(0x12, arm_movement)

    control_signal = pid_control(error)

    control_motors(control_signal)

    time.sleep(0.1)
