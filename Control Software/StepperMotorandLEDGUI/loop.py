import RPi.GPIO as GPIO
from StepperMotorClassTwo import StepperMotor
from multiprocessing import Process

steppermotor = StepperMotor()

def XMove():
    for i in range(1):
        steppermotor.XMoveLeft()
        steppermotor.XMoveRight()
        
def YMove():
    for i in range(1):
        steppermotor.YMoveUp()
        steppermotor.YMoveDown()
        
def ZMove():
    for i in range(1):
        steppermotor.ZMoveUp()
        steppermotor.ZMoveDown()
        
if __name__ == '__main__':        
    Process(target=XMove).start()
    Process(target=YMove).start()
    Process(target=ZMove).start()

