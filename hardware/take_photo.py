#!/usr/bin/python3.4
"""Let's take a photo!."""

from os import rename, path, listdir
from shutil import move
from picamera import PiCamera
from time import sleep

DIR = 'images'
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()

move('image.jpg', 'images/image' + str(len(listdir(DIR)))  + '.jpg')
