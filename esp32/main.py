from machine import Pin  # type: ignore
from time import sleep
import network  # type: ignore
import socket
from modules import bfs
from modules import move
import ujson # type: ignore

SSID = "Unimagdalena"
PASSWORD = ""
COMPASS = 3
MAZE = [
    [0b1001, 0b0001, 0b0011, 0b0111, 0b1100, 0b1001, 0b0011, 0b0101],
    [0b1100, 0b1100, 0b1001, 0b0001, 0b0110, 0b1000, 0b0111, 0b1100],
    [0b1100, 0b1010, 0b0100, 0b1010, 0b0011, 0b0100, 0b1011, 0b0100],
    [0b1000, 0b0111, 0b1000, 0b0011, 0b0101, 0b1000, 0b0101, 0b1100],
    [0b1100, 0b1011, 0b0100, 0b1001, 0b0010, 0b0110, 0b1100, 0b1100],
    [0b1010, 0b0111, 0b1110, 0b1110, 0b1011, 0b0011, 0b0010, 0b0110],
]

def connect(SSID, PASSWORD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Conectando al Wi-Fi...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            pass
    print("Network config:", wlan.ifconfig())

def robot_move(delta, compass):
    RIGHT = [(0, 3), (1, 2), (2, 0), (3, 1)]
    LEFT = [(0, 2), (1, 3), (2, 1), (3, 0)]

    for shift in delta:
        if compass == shift:
            print("CONTINUE")
            move.up()
        elif (compass, shift) in LEFT:
            print("TURN LEFT AND CONTINUE")
            move.left()
            compass = shift
        elif (compass, shift) in RIGHT:
            print("TURN RIGHT AND CONTINUE")
            move.right()
            compass = shift
        else:
            print("TURN 180° AND CONTINUE")
            move.turn()
            compass = shift
        sleep(1)

def handle_request(client_sock):
    request = client_sock.recv(1024)
    request_lines = request.decode().split("\r\n")
    
    headers = {}
    body = ""
    in_body = False
    for line in request_lines:
        if in_body:
            body += line
        elif line == "":
            in_body = True
        else:
            parts = line.split(": ", 1)
            if len(parts) == 2:
                headers[parts[0]] = parts[1]
    
    if "Content-Length" in headers:
        content_length = int(headers["Content-Length"])
        data = ujson.loads(body[:content_length])
        
        if "data" in data:
            start = tuple(data["data"]["START"])
            end = tuple(data["data"]["END"])
            compass = int(data["data"]["COMPASS"])
            
            # Procesar los datos recibidos
            delta = bfs.find(MAZE, start, end)
            response = {"status": "success", "delta": delta}
            robot_move(delta, compass)
        else:
            response = {"status": "error", "message": "Invalid data format"}
    else:
        response = {"status": "error", "message": "Content-Length missing"}
    
    response_data = ujson.dumps(response)
    client_sock.send("HTTP/1.1 200 OK\r\n")
    client_sock.send("Content-Type: application/json\r\n")
    client_sock.send(f"Content-Length: {len(response_data)}\r\n")
    client_sock.send("\r\n")
    client_sock.send(response_data)
    client_sock.close()

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    server_sock = socket.socket()
    server_sock.bind(addr)
    server_sock.listen(5)
    
    print("Server listening on 0.0.0.0:80")
    
    while True:
        client_sock, client_addr = server_sock.accept()
        print("Client connected from", client_addr)
        handle_request(client_sock)

def run():
    connect(SSID, PASSWORD)
    start_server()

if __name__ == "__main__":
    run()

