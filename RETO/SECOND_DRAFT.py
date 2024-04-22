import time
import RPi.GPIO as GPIO
import smbus  # Importar la biblioteca para el bus I2C
from mpu6050 import mpu6050

# Configurar los puertos I2C para los sensores MPU6050
sensor_left = mpu6050(0x68)  # Dirección del sensor MPU6050 izquierdo
sensor_right = mpu6050(0x69)  # Dirección del sensor MPU6050 derecho

# Configuración de los pines GPIO para los puentes H y los motores
motor_left_pin1 = 17
motor_left_pin2 = 18
motor_right_pin1 = 23
motor_right_pin2 = 24

# Inicializar los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_left_pin1, GPIO.OUT)
GPIO.setup(motor_left_pin2, GPIO.OUT)
GPIO.setup(motor_right_pin1, GPIO.OUT)
GPIO.setup(motor_right_pin2, GPIO.OUT)

# Configuración de los objetos PWM para los motores
motor_left_pwm = GPIO.PWM(motor_left_pin1, 1000)
motor_right_pwm = GPIO.PWM(motor_right_pin1, 1000)

# Iniciar los objetos PWM con un ciclo de trabajo del 0% para detener los motores
motor_left_pwm.start(0)
motor_right_pwm.start(0)

# Parámetros del controlador PID
Kp = 1.0  # Ganancia proporcional
Ki = 0.1  # Ganancia integral
Kd = 0.01  # Ganancia derivativa

# Variables para el controlador PID
error_prev = 0
integral = 0

# Definir un umbral para determinar el sentido de movimiento
UMBRAL_MOVIMIENTO = 1.0  # Ajusta este valor según sea necesario

# Configurar la comunicación I2C
bus = smbus.SMBus(1)  # El número 1 indica que se está utilizando el bus I2C 1

# Función para calcular la señal de control con el controlador PID
def pid_control(error):
    global integral, error_prev
    integral += error
    derivative = error - error_prev
    output = Kp * error + Ki * integral + Kd * derivative
    error_prev = error
    return output

# Función para controlar los motores con la señal de control
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

# Definir función para determinar el sentido de movimiento de los brazos
def detect_arm_movement(inclination_left, inclination_right):
    if inclination_left > inclination_right:
        return 1  # Brazo izquierdo se abre, brazo derecho se cierra
    elif inclination_left < inclination_right:
        return 2  # Brazo izquierdo se cierra, brazo derecho se abre
    else:
        return 0  # Ambos brazos se mueven en la misma dirección o están en reposo

# Loop principal
while True:
    # Lectura de datos de los sensores MPU6050
    gyro_left = sensor_left.get_gyro_data()
    gyro_right = sensor_right.get_gyro_data()

    # Calcular la inclinación en cada lado de la suspensión (eje z)
    inclination_left = gyro_left['z']
    inclination_right = gyro_right['z']

    # Calcular el error de inclinación entre los dos lados
    error = inclination_left - inclination_right

    # Detectar el sentido de movimiento de los brazos
    arm_movement = detect_arm_movement(inclination_left, inclination_right)

    # Enviar la señal a través del bus I2C
    bus.write_byte(0x12, arm_movement)  # Dirección y valor de la señal a enviar (cambia 0x12 por la dirección del otro dispositivo)

    # Aplicar control PID para obtener la señal de control
    control_signal = pid_control(error)

    # Controlar los motores con la señal de control
    control_motors(control_signal)

    # Esperar un tiempo antes de la siguiente iteración
    time.sleep(0.1)  # Ajusta el tiempo de espera según sea necesario
