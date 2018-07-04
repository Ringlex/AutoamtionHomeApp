#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
#time.sleep(0.1)
GPIO.output(12,GPIO.HIGH)
#time.sleep(1)
#GPIO.cleanup()
