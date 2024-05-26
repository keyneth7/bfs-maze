from machine import Pin
from time import sleep
import network
import socket

# Conectar a la red Wi-Fi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("MazeRunner", "12345678")

# Esperar a que la conexión se establezca
while not sta_if.isconnected():
    sleep(1)

print('Network config:', sta_if.ifconfig())

# Configurar el LED
led = Pin(2, Pin.OUT)

# Crear el servidor HTTP
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

def handle_client(client):
    request = client.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    # Controlar el LED mediante el servidor web
    if '/led/on' in request:
        led.value(1)
    if '/led/off' in request:
        led.value(0)

    response = """HTTP/1.1 200 OK

<html>
    <head> <title>ESP32 Web Server</title> </head>
    <body> <h1>ESP32 Web Server</h1>
        <p>LED state: %s</p>
        <p><a href="/led/on">Turn On</a></p>
        <p><a href="/led/off">Turn Off</a></p>
    </body>
</html>
""" % ("ON" if led.value() else "OFF")
    
    client.send(response)
    client.close()

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    handle_client(cl)