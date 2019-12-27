#!/usr/bin/python3.8

import time

"""Let's take a photo!."""

from os import rename, path, listdir
from shutil import move
from picamera import PiCamera
from time import sleep

DIR = 'images'
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture(f'{DIR}/image({time.time()}).jpg')
camera.stop_preview()
