import paho.mqtt.suscribe as suscribir
import sys
arreglo=[]
print("Esperando mensajes y conexiones")
while True:
    mensaje = suscribir.simple("iot", hostname="192.168.0.109")
    print("LLEGO ", mensaje.payload)
    dat_recibido=str(mensaje.payload)
    arreglo=dato_recibido.split("@")
    print(arreglo)
    print("La lectura ", arreglo[2])