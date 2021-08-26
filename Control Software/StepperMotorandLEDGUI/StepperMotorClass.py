#stepper motor class

import time
import sys
from threading import Thread
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
        
        self.steps = 200
        
    def ChangeStepsPerClick(self,steps):
        self.steps = steps
        return self
    
    def XMoveLeftStart(self):
        self.xlstopped = False
        xl = Thread(target=self.XMoveLeft, args=())
        xl.daemon = True
        xl.start()
        return self        
    
    def XMoveLeft(self):       
        if self.xlstopped:
            return      
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)
        self.xlstopped = True
        
    def XMoveRightStart(self):
        self.xrstopped = False
        xr = Thread(target=self.XMoveRight, args=())
        xr.daemon = True
        xr.start()
        return self 
        
    def XMoveRight(self):      
        if self.xrstopped:
            return
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M0Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M0Pins:
            GPIO.output(pin, 0)
        self.xrstopped = True
        
    def YMoveUpStart(self):
        self.yustopped = False
        yu = Thread(target=self.YMoveUp, args=())
        yu.daemon = True
        yu.start()
        return self

    def YMoveUp(self):        
        if self.yustopped:
            return
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
        self.yustopped = True
        
    def YMoveDownStart(self):
        self.ydstopped = False
        yd = Thread(target=self.YMoveDown, args=())
        yd.daemon = True
        yd.start()
        return self
        
    def YMoveDown(self):        
        if self.ydstopped:
            return
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M2Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M2Pins:
            GPIO.output(pin, 0)
        self.ydstopped = True
        
    def ZMoveUpStart(self):
        self.zustopped = False
        zu = Thread(target=self.ZMoveUp, args=())
        zu.daemon = True
        zu.start()
        return self
        
    def ZMoveUp(self):
        if self.zustopped:
            return
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seq[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)
        self.zustopped = True
        
    def ZMoveDownStart(self):
        self.zdstopped = False
        zd = Thread(target=self.ZMoveDown, args=())
        zd.daemon = True
        zd.start()
        return self
        
    def ZMoveDown(self):
        if self.zdstopped:
            return
        for i in range (self.steps):
            for halfstep in range(8):
                for pin in range(4):
                    GPIO.output(self.M3Pins[pin], self.seqreversed[halfstep][pin])
                    time.sleep(0.001)
        for pin in self.M3Pins:
            GPIO.output(pin, 0)
        self.zdstopped = True

                