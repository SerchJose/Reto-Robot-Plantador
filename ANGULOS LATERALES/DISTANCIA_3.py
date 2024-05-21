import time
import board
import busio
import adafruit_vl53l0x

# Initialize I2C bus and sensor
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget (in ms)
vl53.measurement_timing_budget = 200000

# Read distance
try:
    while True:
        distance = vl53.range
        print(f"Distance: {distance} mm")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped by User")
