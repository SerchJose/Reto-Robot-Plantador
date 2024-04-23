from mpu6050 import mpu6050
import math
import time

sensor = mpu6050(0x68)  # Dirección I2C del MPU-6050

def calibrar_giroscopio():
    print("Coloca el sensor en una posición horizontal y estable. Calibrando...")
    time.sleep(2)  # Espera unos segundos para que se estabilice
    offset_x = 0
    offset_y = 0
    offset_z = 0
    for _ in range(100):  # Realizar 100 lecturas para calcular el promedio
        gyro_data = sensor.get_gyro_data()
        offset_x += gyro_data['x']
        offset_y += gyro_data['y']
        offset_z += gyro_data['z']
        time.sleep(0.01)  # Espera 10ms entre cada lectura
    offset_x /= 100
    offset_y /= 100
    offset_z /= 100
    print("Calibración completada.")
    return offset_x, offset_y, offset_z

def obtener_inclinacion(offset_x, offset_y, offset_z):
    gyro_data = sensor.get_gyro_data()
    inclinacion_x = math.degrees(math.atan2(gyro_data['x'] - offset_x, gyro_data['z']))
    inclinacion_y = math.degrees(math.atan2(gyro_data['y'] - offset_y, gyro_data['z']))
    return inclinacion_x, inclinacion_y

try:
    offset_x, offset_y, offset_z = calibrar_giroscopio()
    print(f"Offset X: {offset_x}, Offset Y: {offset_y}, Offset Z: {offset_z}")
    while True:
        inclinacion_x, inclinacion_y = obtener_inclinacion(offset_x, offset_y, offset_z)
        print(f'Ángulo de inclinación X: {inclinacion_x} grados, Ángulo de inclinación Y: {inclinacion_y} grados')
        time.sleep(0.1)  # Espera 100ms antes de la siguiente lectura
except KeyboardInterrupt:
    print('Programa detenido por el usuario')