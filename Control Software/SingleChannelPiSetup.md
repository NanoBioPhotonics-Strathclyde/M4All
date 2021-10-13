# Setting Up a Raspberry Pi for a Single Channel Microscope

Firstly set up the Raspberry Pi and install Raspberry Pi OS (32-bit) according to the instructions on the official Raspberry Pi website (https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/0).

Connect to a network following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

The OS doesn't use Python 3 by default and so follow the instructions here to use Python 3 and install pip: https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all

Now open a terminal on the Raspberry Pi and install the following:

* PyQt5: sudo apt-get install python3-pyqt5
* qt5-default: sudo apt-get install qt5-default
* qtcreator: sudo apt-get install qtcreator
* OpenCV: pip install opencv-contrib-python

All other packages such as numpy, RPi.GPIO, threading etc. should already be installed with Raspberry Pi OS.



