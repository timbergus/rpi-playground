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
    for i in range(0, numTimes):
        print "Iteration " + str(i + 1)
        ledON(random.choice(leds))
        time.sleep(speed / 1000)
        ledOFF(random.choice(leds))
        time.sleep(speed / 1000)
    print "Done"
    GPIO.cleanup()


iterations = raw_input("Enter total number of blinks: ")
speed = raw_input("Enter blinking time: ")


Blink(int(iterations), float(speed))
