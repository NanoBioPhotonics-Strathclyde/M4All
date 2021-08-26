import time
import RPi.GPIO as GPIO

class StepperMotor():
    def __init__(self):
        
        #Use BCM GPIO references
        GPIO.setmode(GPIO.BCM)

        #Define GPIO signals to use

        self.M0Pins = [17,18,27,22]
        #self.M1Pins = [4,25,24,23]
        self.M2Pins = [13,12,6,5]
        self.M3Pins = [20,26,16,19]

        #Set all pins as output
        for pin in self.M0Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)

        #for pin in self.M1Pins:
            #GPIO.setup(pin,GPIO.OUT)
            #GPIO.output(pin, 0)

        for pin in self.M2Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)

        for pin in self.M3Pins:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin, 0)   

        #Define step sequence
        self.seq = [[1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1],
               [1,0,0,1]]
        
        #Define reversed step sequence
        self.seqreversed = [[1,0,0,1],
                       [0,0,0,1],
                       [0,0,1,1],
                       [0,0,1,0],
                       [0,1,1,0],
                       [0,1,0,0],
                       [1,1,0,0],
                       [1,0,0,0]]
        
        self.xysteps = 100
        self.zsteps = 20
        
    def XMoveLeft(self):            
        for i in range (self.xysteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)

    def XMoveRight(self):      
        for i in range (self.xysteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)
            
    def YMoveUp(self):        
        for i in range (self.xysteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
            
    def YMoveDown(self):        
        for i in range (self.xysteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
            
    def ZMoveUp(self):
        for i in range (self.zsteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)

    def ZMoveDown(self):
        for i in range (self.zsteps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)