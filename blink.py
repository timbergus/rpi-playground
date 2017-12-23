#!/usr/bin/python3.4
"""Let's blink!."""

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT) # blue
GPIO.setup(35, GPIO.OUT) # green
GPIO.setup(37, GPIO.OUT) # blue

def red(status):
    """Set red color output."""
    GPIO.output(33, status)

def green(status):
    """Set green color output."""
    GPIO.output(35, status)

def blue(status):
    """Set blue color output."""
    GPIO.output(37, status)

def led_on(led):
    """Turn on a led."""
    GPIO.output(led, True)

def led_off(led):
    """Turn off a led."""
    GPIO.output(led, False)

def blink(iterations, speed):
    """Makes the led blink."""
    leds = [33, 35, 37]
    for i in range(0, iterations):
        print("Iteration " + str(i + 1))
        led_on(random.choice(leds))
        time.sleep(speed / 1000)
        led_off(random.choice(leds))
        time.sleep(speed / 1000)
    print("Done")
    GPIO.cleanup()

def main():
    ITERATIONS = input("Enter total number of blinks: ")
    SPEED = input("Enter blinking time: ")
    blink(int(ITERATIONS), float(SPEED))

if __name__ == "__main__":
    main()
