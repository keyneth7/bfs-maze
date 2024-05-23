from machine import Pin  # type: ignore
from time import sleep
from modules import bfs
from modules import move
import network  # type: ignore
import socket

SSID = "Unimagdalena"
PASSWORD = ""
START, END = (3, 1), (0, 4)
MAZE = [
    [0b1001, 0b0001, 0b0011, 0b0111, 0b1100, 0b1001, 0b0011, 0b0101],
    [0b1100, 0b1100, 0b1001, 0b0001, 0b0110, 0b1000, 0b0111, 0b1100],
    [0b1100, 0b1010, 0b0100, 0b1010, 0b0011, 0b0100, 0b1011, 0b0100],
    [0b1000, 0b0111, 0b1000, 0b0011, 0b0101, 0b1000, 0b0101, 0b1100],
    [0b1100, 0b1011, 0b0100, 0b1001, 0b0010, 0b0110, 0b1100, 0b1100],
    [0b1010, 0b0111, 0b1110, 0b1110, 0b1011, 0b0011, 0b0010, 0b0110],
]


def do_connect(SSID, PASSWORD):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Conectando al Wi-Fi...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            pass
    print("Network config:", wlan.ifconfig())


def robot_move(path):
    if path:
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        current = 3

        for i in range(len(path) - 1):
            move = tuple(a - b for a, b in zip(path[i], path[i + 1]))
            delta = directions.index(move)
            current = robot_turn(delta, current)
            sleep(1)
    else:
        print("No se encontró una ruta válida.")


def robot_turn(delta, current):
    right = [(0, 3), (1, 2), (2, 0), (3, 1)]
    left = [(0, 2), (1, 3), (2, 1), (3, 0)]

    if current == delta:
        print("CONTINUE")
        move.up()

    elif (current, delta) in left:
        print("TURN LEFT AND CONTINUE")
        current = delta
        move.left()

    elif (current, delta) in right:
        print("TURN RIGHT AND CONTINUE")
        current = delta
        move.right()

    else:
        print("TURN 180° AND CONTINUE")
        move.turn()

    return current


def run():
    do_connect(SSID, PASSWORD)

    path = bfs.find_path(START, END, MAZE)
    try:
        robot_move(path)
    except KeyboardInterrupt:
        move.stop()
    finally:
        move.stop()


if __name__ == "__main__":
    run()
