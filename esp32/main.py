from machine import Pin  # type: ignore
from time import sleep
from modules import bfs
from modules import move
import network  # type: ignore
import socket

SSID = "Unimagdalena"
PASSWORD = ""
START, END = (3, 1), (0, 4)
CURRENT = 3
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


def movement(delta, current):
    RIGHT = [(0, 3), (1, 2), (2, 0), (3, 1)]
    LEFT = [(0, 2), (1, 3), (2, 1), (3, 0)]

    for shift in delta:

        if current == shift:
            print("CONTINUE")
            move.up()

        elif (current, shift) in LEFT:
            print("TURN LEFT AND CONTINUE")
            move.left()
            current = shift

        elif (current, shift) in RIGHT:
            print("TURN RIGHT AND CONTINUE")
            move.right()
            current = shift
        else:
            print("TURN 180° AND CONTINUE")
            move.turn()
            current = shift


def run():
    connect(SSID, PASSWORD)
    delta = bfs.find(START, END, MAZE)

    try:
        if delta:
            movement(delta, CURRENT)
        else:
            move.invalid()
    except KeyboardInterrupt:
        move.stop()
    finally:
        move.stop()


if __name__ == "__main__":
    run()
