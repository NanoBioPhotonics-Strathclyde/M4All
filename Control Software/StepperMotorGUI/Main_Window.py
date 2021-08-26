# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:56:14 2020

@author: Gemma
"""
import sys
import time 
import cv2
import numpy as np
import RPi.GPIO as GPIO

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, QTimer, QVariant
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QMessageBox

from StepperMotorClass import StepperMotor
from GUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.steppermotor = StepperMotor()
        
#StepperMotorsSignals############################################################################################
        
        self.XMovementLeft.clicked.connect(self.steppermotor.XMoveLeftStart)
        self.XMovementRight.clicked.connect(self.steppermotor.XMoveRightStart)
        
        self.YMovementUp.clicked.connect(self.steppermotor.YMoveUpStart)
        self.YMovementDown.clicked.connect(self.steppermotor.YMoveDownStart)
        
        self.ZMovementUp.clicked.connect(self.steppermotor.ZMoveUpStart)
        self.ZMovementDown.clicked.connect(self.steppermotor.ZMoveDownStart)
        
        self.StepsPerClickSpinBox.valueChanged.connect(self.ChangedSteps)
        
        
#StepperMotorsMethods###############################################################################################
        
    def ChangedSteps(self):
        steps = self.StepsPerClickSpinBox.value()
        self.steppermotor.ChangeStepsPerClick(steps)
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exit(app.exec_())       
        
        
        
        
        
        
        
        
        
        
        
        