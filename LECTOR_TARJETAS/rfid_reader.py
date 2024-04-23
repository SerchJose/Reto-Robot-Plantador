from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

try:
    while True:
        id, text = reader.read()
        print("ID de la tarjeta:", id)
        print("Contenido de la tarjeta:", text)
        
        if text == "tarjeta_correcta":
            # Enciende el LED verde y transmite el mensaje a la computadora
            print("Tarjeta correcta")
        else:
            # Enciende el LED rojo y transmite el mensaje a la computadora
            print("Tarjeta incorrecta")
        
        time.sleep(1)
finally:
    GPIO.cleanup()
