#
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
GPIO.output(12,GPIO.LOW)
#GPIO.cleanup()
