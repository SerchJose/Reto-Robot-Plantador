# Importar la clase mpu6050 del módulo mpu6050
from mpu6050 import mpu6050
# Importar el módulo RPi.GPIO para controlar los pines GPIO de la Raspberry Pi
import RPi.GPIO as GPIO
# Importar el módulo time para manejar el tiempo
import time
# Importar los módulos signal y sys para manejar señales y terminar el programa de manera segura
import signal
import sys

# Configuración de pines GPIO
GPIO.setmode(GPIO.BOARD)
motor_pin1 = 11
motor_pin2 = 12
pwm_pin = 18
# Configurar pines como salida
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)
# Inicializar PWM
pwm = GPIO.PWM(pwm_pin, 100)  # Frecuencia de PWM de 100 Hz
pwm.start(0)  # Iniciar PWM con ciclo de trabajo del 0%

# Inicialización del sensor de giroscopio con dirección I2C 0x68
sensor = mpu6050(0x68)

# Parámetros del controlador PID
Kp = 0.6
Ki = 0.2
Kd = 0.1

# Altura deseada para cada lado de la suspensión (en radianes)
inclinacion_deseada = 0.0

# Función para controlar el motorreductor con PWM
def controlar_motorreductor_pwm(velocidad):
    # Convertir la velocidad a un valor entre 0 y 100 (porcentaje)
    velocidad_pwm = abs(velocidad) * 100
    # Ajustar la dirección del motor
    if velocidad > 0:
        GPIO.output(motor_pin1, GPIO.HIGH)
        GPIO.output(motor_pin2, GPIO.LOW)
    elif velocidad < 0:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.HIGH)
    else:
        GPIO.output(motor_pin1, GPIO.LOW)
        GPIO.output(motor_pin2, GPIO.LOW)
    # Establecer la velocidad del motor con PWM
    pwm.ChangeDutyCycle(velocidad_pwm)

# Función para calcular la salida del controlador PID
def controlador_pid(error, integral, derivativo):
    proporcional = Kp * error
    integral += error
    derivativo = Kd * (error - derivativo)
    return proporcional + Ki * integral + derivativo, integral, error

# Manejador de señales para detener el programa de manera segura
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

# Registra el manejador de señales para la señal SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Bucle de control principal
try:
    while True:
        # Leer datos del sensor de giroscopio
        inclinacion_izquierda = sensor.get_gyro_data()['x']
        inclinacion_derecha = sensor.get_gyro_data()['y']

        # Calcular errores de inclinación
        error_izquierda = inclinacion_deseada - inclinacion_izquierda
        error_derecha = inclinacion_deseada - inclinacion_derecha

        # Calcular salida del controlador PID
        salida_izquierda, integral_izquierda, derivativo_izquierda = controlador_pid(error_izquierda, 0, 0)
        salida_derecha, integral_derecha, derivativo_derecha = controlador_pid(error_derecha, 0, 0)

        # Aplicar salida del controlador al motorreductor con PWM
        controlar_motorreductor_pwm(salida_izquierda)

        # Pequeño retardo para el bucle de control
        time.sleep(0.01)

except Exception as e:
    print("Error:", e)

finally:
    # Limpiar configuraciones de pines GPIO al salir del programa
    GPIO.cleanup()
