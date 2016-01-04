import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

def Blink(numTimes, speed):
    for i in range(0, numTimes):
        print "Iteration " + str(i + 1)
        GPIO.output(7, True)
        time.sleep(speed / 1000)
        GPIO.output(7, False)
        time.sleep(speed / 1000)
    print "Done"
    GPIO.cleanup()

iterations = raw_input("Enter total number of blinks: ")
speed = raw_input("Enter blinking time: ")

Blink(int(iterations), float(speed))
