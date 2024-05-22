import time
import VL53L0X

# Crear un objeto de la clase VL53L0X
tof = VL53L0X.VL53L0X()

# Iniciar el sensor
tof.start_ranging(VL53L0X.Vl53l0xAccuracyMode.BETTER)

timing = tof.get_timing()
if timing < 20000:
    timing = 20000
print("Timing: %d ms" % (timing / 1000))

try:
    while True:
        distance = tof.get_distance()
        if distance > 0:
            print("Distancia medida: %d mm" % distance)
        else:
            print("Error al medir la distancia")
        time.sleep(timing / 1000000.00)
except KeyboardInterrupt:
    pass

tof.stop_ranging()
