import time
import smbus2
import VL53L0X

# Initialize the I2C bus (use 1 for Raspberry Pi 4)
bus = smbus2.SMBus(1)

# Create a VL53L0X object
tof = VL53L0X.VL53L0X(i2c=bus)

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_GOOD_ACCURACY_MODE)

# Read distance
try:
    while True:
        distance = tof.get_distance()
        print(f"Distance: {distance} mm")
        time.sleep(0.5)
except KeyboardInterrupt:
    # Stop ranging on Ctrl+C
    tof.stop_ranging()
