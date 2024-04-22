#sudo raspi-config
#Select option 5 'interfacing options'
#Select I2C
#Enable all
#i2cdetect -y 1 'Se detecta correctamente si sale un 68'
#instalar 'sudo apt install python3-smbus'
#instalar 'pip install mpu6050-raspberrypi'
#abrir ventana para programar con el comando 'nano_6050.py'

from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

while True:
    print("Sistema encendido y funcionando")
    print()

    print("Temp: "+str(mpu.get_temp()))
    print()

    accel_data = mpu.get_accel_data()
    print("Aceleracion en X: "+str(accel_data['x']))
    print("Aceleracion en Y: "+str(accel_data['y']))
    print("Aceleracion en Z: "+str(accel_data['z']))
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str(gyro_data['x']))
    print("Gyro X : "+str(gyro_data['y']))
    print("Gyro X : "+str(gyro_data['z']))
    print()

    print ("-------------------------------")

    time.sleep(1)