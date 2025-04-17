import paho.mqtt.publish as publish

# IP de la Raspberry Pi
broker = "192.168.84.231"  # reemplaza con la IP real de tu Raspberry

print("Escribe 'on' para encender, 'off' para apagar el LED o 'salir' para terminar el programa.\n")

while True:
    mensaje = input("Mensaje a enviar: ").strip().lower()
    
    if mensaje == "salir":
        print("Saliendo del programa...")
        break
    elif mensaje in ["on", "off"]:
        publish.single("casa/led", mensaje, hostname=broker)
        print(f"Mensaje '{mensaje}' enviado al broker {broker}")
    else:
        print("Comando no válido. Usa 'on', 'off' o 'salir'.")
