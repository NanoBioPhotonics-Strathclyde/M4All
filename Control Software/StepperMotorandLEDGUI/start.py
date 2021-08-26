# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:17:07 2020

@author: Gemma
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from StepperMotorClass import StepperMotor
from ledclass import LED
from TimelapseClass import Timelapse
from Main_Window import MainWindow

steppermotor = StepperMotor()
led = LED()
timelapse = Timelapse()

app = QApplication([])
start_window = MainWindow()
start_window.show()
app.exit(app.exec_())