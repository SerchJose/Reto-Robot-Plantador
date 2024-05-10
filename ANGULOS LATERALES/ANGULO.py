import time
import math
import RPi.GPIO as GPIO

# Definir los pines GPIO para el sensor VL53L0X
SCL_PIN = 23
SDA_PIN = 24

# Longitud de la hipotenusa (en mm)
HIPOTENUSA = 100

# Función para inicializar los pines GPIO
def init_gpio():
    GPIO.setmode(GPIO.BCM)  # Configura los pines GPIO utilizando el modo de numeración BCM
    GPIO.setup(SCL_PIN, GPIO.OUT)  # Configura el pin SCL como salida
    GPIO.setup(SDA_PIN, GPIO.OUT)  # Configura el pin SDA como salida

# Función para enviar un bit a través de GPIO
def send_bit(bit):
    GPIO.output(SDA_PIN, bit)  # Establece el estado del pin SDA
    GPIO.output(SCL_PIN, GPIO.HIGH)  # Establece el pin SCL en alto para enviar el bit
    time.sleep(0.1)  # Espera un corto tiempo
    GPIO.output(SCL_PIN, GPIO.LOW)  # Establece el pin SCL en bajo después de enviar el bit

# Función para enviar un byte a través de GPIO
def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)  # Envía cada bit del byte

# Función para iniciar la comunicación con el sensor VL53L0X
def start_communication():
    GPIO.output(SDA_PIN, GPIO.HIGH)  # Establece el pin SDA en alto
    GPIO.output(SCL_PIN, GPIO.HIGH)  # Establece el pin SCL en alto
    GPIO.output(SDA_PIN, GPIO.LOW)  # Envía una señal de inicio
    GPIO.output(SCL_PIN, GPIO.LOW)  # Establece el pin SCL en bajo después del inicio
    GPIO.output(SCL_PIN, GPIO.HIGH)  # Restablece el pin SCL en alto
    GPIO.output(SDA_PIN, GPIO.HIGH)  # Restablece el pin SDA en alto
    GPIO.output(SCL_PIN, GPIO.LOW)  # Establece el pin SCL en bajo después del inicio

# Función para leer un byte del sensor VL53L0X
def read_byte():
    GPIO.setup(SDA_PIN, GPIO.IN)  # Configura el pin SDA como entrada
    byte = 0
    for i in range(8):
        GPIO.output(SCL_PIN, GPIO.HIGH)  # Establece el pin SCL en alto para recibir un bit
        bit = GPIO.input(SDA_PIN)  # Lee el estado del pin SDA
        byte = (byte << 1) | bit  # Agrega el bit leído al byte
        GPIO.output(SCL_PIN, GPIO.LOW)  # Establece el pin SCL en bajo después de recibir el bit
    GPIO.setup(SDA_PIN, GPIO.OUT)  # Restablece el pin SDA como salida
    return byte

# Función para leer la distancia del sensor VL53L0X
def read_distance():
    start_communication()  # Inicia la comunicación con el sensor
    send_byte(0xC0)  # Envía la dirección y el comando para iniciar la lectura de distancia
    send_byte(0x04)  # Envía datos adicionales para la lectura
    send_byte(0x03)  # Envía datos adicionales para la lectura
    send_byte(0x03)  # Envía datos adicionales para la lectura
    send_byte(0x03)  # Envía datos adicionales para la lectura
    send_byte(0x00)  # Envía datos adicionales para la lectura
    send_byte(0x00)  # Envía datos adicionales para la lectura
    send_byte(0x00)  # Envía datos adicionales para la lectura
    start_communication()  # Inicia una nueva comunicación con el sensor
    send_byte(0xC1)  # Envía la dirección para leer la distancia
    distance_low = read_byte()  # Lee el byte de menor orden de la distancia
    distance_high = read_byte()  # Lee el byte de mayor orden de la distancia
    distance = (distance_high << 8) | distance_low  # Combina los bytes para obtener la distancia
    return distance

if __name__ == "__main__":
    try:
        init_gpio()  # Inicializa los pines GPIO
        while True:
            distance = read_distance()  # Lee la distancia del sensor
            angle = math.degrees(math.acos(distance / HIPOTENUSA))  # Calcula el ángulo
            print("Distance: {} mm, Angle: {} degrees".format(distance, angle))  # Muestra la distancia y el ángulo
            time.sleep(1)  # Espera un segundo
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()  # Limpia los pines GPIO al finalizar el programa
