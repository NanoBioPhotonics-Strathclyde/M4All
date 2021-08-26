import RPi.GPIO as GPIO
import time

class LED():
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(23,GPIO.OUT)
        
    def LEDon(self):
        
        GPIO.output(23,GPIO.HIGH)
        
    def LEDoff(self):
        
        GPIO.output(23,GPIO.LOW)
