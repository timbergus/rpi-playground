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
    """Turn LED on."""
    GPIO.output(led, True)

def led_off(led):
    """Turn LED off."""
    GPIO.output(led, False)

def blink(iterations, speed):
    """Makes the led blink."""
    leds = [33, 35, 37]
    last_led_01 = 33
    last_led_02 = 35
    for i in range(iterations):
        print("Iteration " + str(i + 1))
        random_led_01 = random.choice(leds)
        random_led_02 = random.choice(leds)
        while random_led_01 == last_led_01 or random_led_02 == last_led_02 or random_led_01 == random_led_02:
            random_led_01 = random.choice(leds)
            random_led_02 = random.choice(leds)
        last_led_01 = random_led_01
        last_led_02 = random_led_02
        led_on(last_led_01)
        led_on(last_led_02)
        time.sleep(speed / 1000)
        led_off(last_led_01)
        led_off(last_led_02)
        time.sleep(speed / 1000)
    print("Done")
    GPIO.cleanup()

def main():
    """MAIN"""
    iterations = input("Enter total number of blinks: ")
    speed = input("Enter blinking time: ")
    blink(int(iterations), float(speed))

if __name__ == "__main__":
    main()
