#!/usr/bin/python3.4
"""Let's blink!."""

from picamera import PiCamera
from time import sleep

CAMERA = PiCamera()

CAMERA.start_preview()
sleep(5)
CAMERA.capture('image.jpg')
CAMERA.stop_preview()
