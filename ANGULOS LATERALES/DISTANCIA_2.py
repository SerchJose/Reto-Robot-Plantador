import time
import VL53L0X

# Inicializa el sensor VL53L0X
tof = VL53L0X.VL53L0X()

# Inicia el sensor en modo de medición continua
tof.start_ranging(VL53L0X.VL53L0X_GOOD_ACCURACY_MODE)

try:
    while True:
        # Realiza una nueva medición de distancia
        distance = tof.get_distance()

        # Imprime la distancia en milímetros
        print("Distancia: {} mm".format(distance))

        # Espera un corto período antes de realizar la próxima medición
        time.sleep(0.1)

except KeyboardInterrupt:
    # Maneja la interrupción del teclado (Ctrl+C) para salir limpiamente
    tof.stop_ranging()
    print("\nPrograma detenido por el usuario.")
