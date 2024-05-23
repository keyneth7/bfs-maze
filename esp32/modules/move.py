from machine import Pin, PWM  # type: ignore
import time

LEFT_SERVO_PIN = 14
RIGHT_SERVO_PIN = 27

left_servo = PWM(Pin(LEFT_SERVO_PIN), freq=50)
right_servo = PWM(Pin(RIGHT_SERVO_PIN), freq=50)


def stop():
    left_servo.duty(77)
    right_servo.duty(77)


def left():
    left_servo.duty(40)
    right_servo.duty(100)


def right():
    left_servo.duty(100)
    right_servo.duty(40)


def up():
    left_servo.duty(100)
    right_servo.duty(100)


def turn():
    left_servo.duty(40)
    right_servo.duty(100)
    time.sleep(1)
    stop()
