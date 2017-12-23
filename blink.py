import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT) # blue
GPIO.setup(35, GPIO.OUT) # green
GPIO.setup(37, GPIO.OUT) # blue


def red(status):
    GPIO.output(33, status)


def green(status):
    GPIO.output(35, status)


def blue(status):
    GPIO.output(37, status)


def ledON(led):
    GPIO.output(led, True)


def ledOFF(led):
    GPIO.output(led, False)

leds = [33, 35, 37]

def Blink(numTimes, speed):
    last_led_01 = 33
    last_led_02 = 35
    for i in range(numTimes):
        print("Iteration " + str(i + 1))
        random_led_01 = random.choice(leds)
        random_led_02 = random.choice(leds)
        while random_led_01 == last_led_01 or random_led_02 == last_led_02 or random_led_01 == random_led_02:
            random_led_01 = random.choice(leds)
            random_led_02 = random.choice(leds)
        last_led_01 = random_led_01
        last_led_02 = random_led_02
        ledON(last_led_01)
        ledON(last_led_02)
        time.sleep(speed / 1000)
        ledOFF(last_led_01)
        ledOFF(last_led_02)
        time.sleep(speed / 1000)
    print("Done")
    GPIO.cleanup()


iterations = input("Enter total number of blinks: ")
speed = input("Enter blinking time: ")


Blink(int(iterations), float(speed))
