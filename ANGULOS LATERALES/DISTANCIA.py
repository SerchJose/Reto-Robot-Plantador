import RPi.GPIO as GPIO
import time

# Definir los pines GPIO para el sensor VL53L0X
SCL_PIN = 23
SDA_PIN = 24

# Función para inicializar los pines GPIO
def init_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SCL_PIN, GPIO.OUT)
    GPIO.setup(SDA_PIN, GPIO.OUT)

# Función para enviar un bit a través de GPIO
def send_bit(bit):
    GPIO.output(SDA_PIN, bit)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(SCL_PIN, GPIO.LOW)

# Función para enviar un byte a través de GPIO
def send_byte(byte):
    for i in range(8):
        send_bit((byte >> (7 - i)) & 1)

# Función para iniciar la comunicación con el sensor VL53L0X
def start_communication():
    GPIO.output(SDA_PIN, GPIO.HIGH)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    GPIO.output(SDA_PIN, GPIO.LOW)
    GPIO.output(SCL_PIN, GPIO.LOW)
    GPIO.output(SCL_PIN, GPIO.HIGH)
    GPIO.output(SDA_PIN, GPIO.HIGH)
    GPIO.output(SCL_PIN, GPIO.LOW)

# Función para leer un byte del sensor VL53L0X
def read_byte():
    GPIO.setup(SDA_PIN, GPIO.IN)
    byte = 0
    for i in range(8):
        GPIO.output(SCL_PIN, GPIO.HIGH)
        bit = GPIO.input(SDA_PIN)
        byte = (byte << 1) | bit
        GPIO.output(SCL_PIN, GPIO.LOW)
    GPIO.setup(SDA_PIN, GPIO.OUT)
    return byte

# Función para leer la distancia del sensor VL53L0X
def read_distance():
    start_communication()
    send_byte(0xC0)
    send_byte(0x04)
    send_byte(0x03)
    send_byte(0x03)
    send_byte(0x03)
    send_byte(0x00)
    send_byte(0x00)
    send_byte(0x00)
    start_communication()
    send_byte(0xC1)
    distance_low = read_byte()
    distance_high = read_byte()
    distance = (distance_high << 8) | distance_low
    return distance

if __name__ == "__main__":
    try:
        init_gpio()
        while True:
            distance = read_distance()
            print("Distance: {} mm".format(distance))
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
