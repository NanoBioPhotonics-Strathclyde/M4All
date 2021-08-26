# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:56:14 2020

@author: Gemma
"""
import sys
import time 
import numpy as np
import RPi.GPIO as GPIO

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QThread, QTimer, QVariant
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QMessageBox, QDialog, QFileDialog

from StepperMotorClass import StepperMotor
from ledclass import LED
from TimelapseClass import Timelapse
from GUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.steppermotor = StepperMotor()
        self.led = LED()
        self.timelapse = Timelapse()
        
#StepperMotorsSignals############################################################################################
        
        self.XMovementLeft.clicked.connect(self.steppermotor.XMoveLeftStart)
        self.XMovementRight.clicked.connect(self.steppermotor.XMoveRightStart)
        
        self.YMovementUp.clicked.connect(self.steppermotor.YMoveUpStart)
        self.YMovementDown.clicked.connect(self.steppermotor.YMoveDownStart)
        
        self.ZMovementUp.clicked.connect(self.steppermotor.ZMoveUpStart)
        self.ZMovementDown.clicked.connect(self.steppermotor.ZMoveDownStart)
        
        self.StepsPerClickSpinBox.valueChanged.connect(self.ChangedSteps)

#LEDSignals############################################################################################
        
        self.LEDOn.clicked.connect(self.led.LEDon)
        self.LEDOff.clicked.connect(self.led.LEDoff)

#TimelapseSignals############################################################################################
        
        self.widthbox.valueChanged.connect(self.ChangedWidth)
        self.heightbox.valueChanged.connect(self.ChangedHeight)
        self.framesbox.valueChanged.connect(self.ChangedFrames)
        self.intervalbox.valueChanged.connect(self.ChangedInterval)
        
        self.browse.clicked.connect(self.BrowseFiles)
        self.filename.textChanged.connect(self.ChangedFile)
        
        self.StartTimelapse.clicked.connect(self.timelapse.StartTimelapseThread)
        
        self.startpreview.clicked.connect(self.timelapse.StartPreviewThread)
        self.stoppreview.clicked.connect(self.timelapse.StopPreview)
        
#StepperMotorsMethods###############################################################################################
        
    def ChangedSteps(self):
        steps = self.StepsPerClickSpinBox.value()
        self.steppermotor.ChangeStepsPerClick(steps)
        
#TimelapseMethods###############################################################################################
        
    def ChangedWidth(self):
        width = self.widthbox.value()
        self.timelapse.ChangeWidth(width)
        
    def ChangedHeight(self):
        height = self.heightbox.value()
        self.timelapse.ChangeHeight(height)
        
    def ChangedFrames(self):
        frames = self.framesbox.value()
        self.timelapse.ChangeNumberOfFrames(frames)
        
    def ChangedInterval(self):
        interval = self.intervalbox.value()
        self.timelapse.ChangeInterval(interval)
        
    def BrowseFiles(self):
        fname=QFileDialog.getExistingDirectory(self, 'Choose save directory', '/home/pi')
        self.filename.setText(fname)
        
    def ChangedFile(self):
        file = self.filename.text()
        self.timelapse.ChangeFile(file)

        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exit(app.exec_())       
        
        
        
        
        
        
        
        
        
        
        
        