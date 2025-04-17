# Robotica2
## Nombres: Cristian Alejandro Durán Ignacio - Alfaro Ayzama José Fernando - Ever Rolando Rejas Espinoza

# 🚀 Proyecto 3

## 💡 Control de LED por MQTT entre Laptop y Raspberry Pi 4
### Este proyecto demuestra cómo comunicar una laptop y una Raspberry Pi mediante el protocolo **MQTT**, utilizando la laptop como **publicador** y la Raspberry Pi como **suscriptor**. A través de comandos enviados por la PC (`on` / `off`), se puede encender o apagar un LED conectado a la Raspberry Pi.

## 📌 Introducción
### Este proyecto permite encender o apagar un LED conectado a una **Raspberry Pi 4** usando comandos enviados desde una **laptop** a través del protocolo **MQTT**. La comunicación se realiza mediante un broker local (Mosquitto) alojado en la Raspberry.  
El objetivo es ilustrar cómo funcionan los roles de **publicador** (laptop) y **suscriptor** (Raspberry Pi) con MQTT en un entorno IoT básico.

## 🧰 Tecnologías y Librerías
- Python 3
  
- MQTT con [paho-mqtt](https://pypi.org/project/paho-mqtt/)
  
- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) para control de pines en la Raspberry Pi
  
- Raspberry Pi 4 con sistema operativo Raspbian
  
- LED, resistencia de 220Ω, cables de conexión

## ⚙️ Esquema de funcionamiento
El esquema muestra cómo la laptop envía comandos al servidor MQTT (Mosquitto), que luego los redirige a la Raspberry Pi para encender o apagar un LED según el mensaje recibido.
Esta arquitectura sigue el modelo publicador-suscriptor del protocolo MQTT.

## 🚀Para armado y utilizacion de codigo
### Clonar el repositorio :  
```bash
git clone https://github.com/Josefer98/Robotica2_.git
```
git clone https://github.com/Josefer98/Robotica2_.git
### Copiar el codigo en un entorno adecuado para python
Para este proyecto se utilzo el editor MU
![Editor MU de Rasbien](files/mu.jpg)
### Instalar dependencias
en la teminal ejecuta:

![comandos](files/comandos.jpg)
### Conectar camara y probar en rasberry
conecta la camara mediante el usb
prueba con este comando:

![comandos](files/pruebacam.jpg)
### Armar brazo robótico
  -usa el pin 17 para el primer servomotor que controlara el movimiento de derecha a izquierda
  
  -usa el pin 18 para el sefundo servomotor que controlara el movimiento de arriba a abajo
  
  -usa el pin 27 para el tercer servomotor que controlara que la garra abra o cierre
  
  -coneccion a tierra importante 

  <p>
  <img src="files/pinesrassberry.jpg" alt="rassberry" width="700" height="500"/>
  </p>
  
  -conecciones:
  
  <p>
  <img src="files/circuito.jpeg" alt="conecciones" width="500" />
  </p>
  
  -brazo armado:

  <p>
  <img src="files/brazo.jpeg" alt="brazo" width="500" height="500"/>
  </p>
  
  -opcional el uso de de una fuente para dar energia solo a los servomotores:

  <p>
  <img src="files/fuente.jpeg" alt="fuente" width="500" height="500"/>
  </p>
  
# 🎥Demostracion de funcionamineto

![Brazo robot](files/demostracion.gif)
