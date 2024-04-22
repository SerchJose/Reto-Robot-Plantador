from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import time
import signal
import sys

GPIO.setmode(GPIO.BOARD)
motor_pin1 = 11
motor_pin2 = 12
pwm_pin = 18
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)

sensor = mpu6050(0x68)

Kp = 0.6
Ki = 0.2
Kd = 0.1

inclinacion_deseada = 0.0

def controlar_motorreductor_pwm(velocidad):
    velocidad_pwm = abs(velocidad) * 100
    if velocidad > 0:
        GPIO.output(motor_pin1, GPIO.HIGH)
        GPIO.output(motor_pin2, GPIO.LOW)
    elif velocidad < 0:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.HIGH)
    else:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.LOW)
    pwm.ChangeDutyCycle(velocidad_pwm)

def controlador_pid(error, integral, derivativo):
    proporcional = Kp * error
    integral += error
    derivativo = Kd * (error - derivativo)
    return proporcional + Ki * integral + derivativo, integral, error

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        inclinacion_izquierda = sensor.get_gyro_data()['x']
        inclinacion_derecha = sensor.get_gyro_data()['y']

        error_izquierda = inclinacion_deseada - inclinacion_izquierda
        error_derecha = inclinacion_deseada - inclinacion_derecha

        salida_izquierda, integral_izquierda, derivativo_izquierda = controlador_pid(error_izquierda, 0, 0)
        salida_derecha, integral_derecha, derivativo_derecha = controlador_pid(error_derecha, 0, 0)

        controlar_motorreductor_pwm(salida_izquierda)

        time.sleep(0.01)

except Exception as e:
    print("Error:", e)

finally:
    GPIO.cleanup()
    