import paho.mqtt.client as mqtt
import time
from datetime import datetime

# Configuración del cliente MQTT
mqtt_broker = "ip_de_tu_esp"
mqtt_port = 1883
mqtt_topic = "sensor/dato"  # El topic debe ser el mismo que en el ESP8266
client = mqtt.Client("raspberry-pi")  # Crea un cliente MQTT

# Función para manejar la recepción de mensajes MQTT
def on_message(client, userdata, message):
    print("Mensaje recibido:", str(message.payload.decode("utf-8")))

# Establece la función de callback
client.on_message = on_message

# Conecta al broker MQTT
client.connect(mqtt_broker, mqtt_port)
client.loop_start()

try:
    while True:
        # Publica un mensaje de solicitud de datos al ESP8266
        client.publish(mqtt_topic, "solicitud_dato")
        
        # Espera a que llegue el mensaje con el dato
        time.sleep(1)
        
        # Muestra la información en pantalla
        print("Desarrollador: Tu nombre")
        print("Dato: El voltaje actual es de:", str(message.payload.decode("utf-8")), "V")
        print("Hora:", datetime.now().strftime("%H:%M:%S"))
        print("----------------------")
except KeyboardInterrupt:
    pass

# Detiene la ejecución del cliente MQTT
client.loop_stop()
client.disconnect()
