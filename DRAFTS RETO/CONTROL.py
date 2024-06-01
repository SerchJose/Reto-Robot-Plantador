import time
import smbus
import RPi.GPIO as GPIO
from mpu6050 import mpu6050

# Define I2C bus
bus = smbus.SMBus(1)

# Define Motor Pins
RPWM1 = 5  # GPIO pin for motor 1 clockwise direction
LPWM1 = 6  # GPIO pin for motor 1 counterclockwise direction
RPWM2 = 7  # GPIO pin for motor 2 clockwise direction
LPWM2 = 8  # GPIO pin for motor 2 counterclockwise direction

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RPWM1, GPIO.OUT)
GPIO.setup(LPWM1, GPIO.OUT)
GPIO.setup(RPWM2, GPIO.OUT)
GPIO.setup(LPWM2, GPIO.OUT)

# Initialize PWM
pwm1_clockwise = GPIO.PWM(RPWM1, 1000)
pwm1_counterclockwise = GPIO.PWM(LPWM1, 1000)
pwm2_clockwise = GPIO.PWM(RPWM2, 1000)
pwm2_counterclockwise = GPIO.PWM(LPWM2, 1000)

pwm1_clockwise.start(0)
pwm1_counterclockwise.start(0)
pwm2_clockwise.start(0)
pwm2_counterclockwise.start(0)

# Initialize MPU6050 sensors
mpu1 = mpu6050(0x68)
mpu2 = mpu6050(0x69)

# Control system variables
kp = 0.5
ki = 0.01
kd = 0.25

intError1 = 0
prevError1 = 0

intError2 = 0
prevError2 = 0

def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

try:
    while True:
        # Read data from the first MPU6050
        accel_data1 = mpu1.get_accel_data()
        gyro_data1 = mpu1.get_gyro_data()
        temp1 = mpu1.get_temp()

        # Read data from the second MPU6050
        accel_data2 = mpu2.get_accel_data()
        gyro_data2 = mpu2.get_gyro_data()
        temp2 = mpu2.get_temp()

        # Extract angles
        in_x1 = accel_data1['x']
        in_y1 = accel_data1['y']
        gz1 = gyro_data1['z']

        in_x2 = accel_data2['x']
        in_y2 = accel_data2['y']
        gz2 = gyro_data2['z']

        reference = 0
        error1 = reference - in_x1
        error2 = reference - in_x2

        print(f"MPU1 - Position: {in_x1}, Error: {error1}")
        print(f"MPU2 - Position: {in_x2}, Error: {error2}")

        # PID Controller Calculations for MPU1
        intError1 += error1
        derError1 = error1 - prevError1
        control1 = kp * error1 + ki * intError1 + kd * derError1
        control1 = constrain(control1, 0, 1)
        prevError1 = error1

        # PID Controller Calculations for MPU2
        intError2 += error2
        derError2 = error2 - prevError2
        control2 = kp * error2 + ki * intError2 + kd * derError2
        control2 = constrain(control2, 0, 1)
        prevError2 = error2

        # Controllers
        if (error1 > 1 and error2 < -1 and error1 < 15 and error2 > -15):
            pwm1_clockwise.ChangeDutyCycle(abs(control1) * 100)
            pwm1_counterclockwise.ChangeDutyCycle(0)
            pwm2_clockwise.ChangeDutyCycle(0)
            pwm2_counterclockwise.ChangeDutyCycle(abs(control1) * 100)

            print(f"Motor 1: Clockwise, Velocity: {abs(control1) * 100}")
            print(f"Motor 2: CounterClockwise, Velocity: {abs(control1) * 100}")

        elif (error1 < -1 and error2 > 1 and error1 > -15 and error2 < 15):
            pwm1_clockwise.ChangeDutyCycle(0)
            pwm1_counterclockwise.ChangeDutyCycle(abs(control2) * 100)
            pwm2_clockwise.ChangeDutyCycle(abs(control2) * 100)
            pwm2_counterclockwise.ChangeDutyCycle(0)

            print(f"Motor 1: CounterClockwise, Velocity: {abs(control2) * 100}")
            print(f"Motor 2: Clockwise, Velocity: {abs(control2) * 100}")

        else:
            pwm1_clockwise.ChangeDutyCycle(0)
            pwm1_counterclockwise.ChangeDutyCycle(0)
            pwm2_clockwise.ChangeDutyCycle(0)
            pwm2_counterclockwise.ChangeDutyCycle(0)

            print("Motors stopped.")

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    pwm1_clockwise.stop()
    pwm1_counterclockwise.stop()
    pwm2_clockwise.stop()
    pwm2_counterclockwise.stop()
    GPIO.cleanup()
