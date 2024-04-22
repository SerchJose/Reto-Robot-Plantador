# Imports
import smbus
import time
import math

# MPU6050 Registers
PWR_MGMT_1 = 0x6B
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47

# Constants
GYRO_SENSITIVITY = 131.0  # Sensitivity of the gyro in degrees per second

# Initialize I2C bus
bus = smbus.SMBus(1)
device_address = 0x68  # MPU6050 address

# Wake up the MPU6050
bus.write_byte_data(device_address, PWR_MGMT_1, 0)

# Read gyro data
def read_gyro(reg):
    gyro_data = bus.read_i2c_block_data(device_address, reg, 2)
    gyro_val = gyro_data[0] << 8 | gyro_data[1]
    return gyro_val

def get_inclination():
    gyro_x = read_gyro(GYRO_XOUT) / GYRO_SENSITIVITY
    gyro_y = read_gyro(GYRO_YOUT) / GYRO_SENSITIVITY
    gyro_z = read_gyro(GYRO_ZOUT) / GYRO_SENSITIVITY
    
    # Integrate gyro values to get inclination angles
    inclination_x += gyro_x * dt
    inclination_y += gyro_y * dt
    inclination_z += gyro_z * dt
    
    return inclination_x, inclination_y, inclination_z

# Initial inclination angles
inclination_x = 0.0
inclination_y = 0.0
inclination_z = 0.0

# Time interval for integration
dt = 0.01  # 10 ms

while True:
    inclination_x, inclination_y, inclination_z = get_inclination()
    print(f"Inclination X: {inclination_x:.2f} degrees, Inclination Y: {inclination_y:.2f} degrees, Inclination Z: {inclination_z:.2f} degrees")
    time.sleep(dt)