from machine import Pin, PWM  # type: ignore
import time

LEFT_SERVO_PIN = 14
RIGHT_SERVO_PIN = 27

left_servo = PWM(Pin(LEFT_SERVO_PIN), freq=50)
right_servo = PWM(Pin(RIGHT_SERVO_PIN), freq=50)

led_pin = Pin(2, Pin.OUT)


def blink_led(duration=0.1):
    led_pin.on()
    time.sleep(duration)
    led_pin.off()


def up():
    left_servo.duty(100)
    right_servo.duty(100)
    blink_led()


def turn():
    left_servo.duty(40)
    right_servo.duty(100)
    time.sleep(1)
    blink_led()
    stop()


def stop():
    left_servo.duty(77)
    right_servo.duty(77)
    blink_led()


def left():
    left_servo.duty(40)
    right_servo.duty(100)
    blink_led()


def right():
    left_servo.duty(100)
    right_servo.duty(40)
    blink_led()


def invalid():
    blink_led()
    print("No hay futuro.")
