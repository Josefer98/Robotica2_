import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

# Configura GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Funcion cuando se recibe un mensaje
def on_message(client, userdata, msg):
    mensaje = msg.payload.decode()
    print(f"Mensaje recibido: {mensaje}")
    if mensaje == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED encendido")
    elif mensaje == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED apagado")

# Configura MQTT
client = mqtt.Client()
client.on_message = on_message

# Conectate al broker
client.connect("localhost", 1883, 60)  # Usa "localhost" porque el broker corre en la Raspberry
client.subscribe("casa/led")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Saliendo...")
finally:
    GPIO.cleanup()