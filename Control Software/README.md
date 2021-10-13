# Control Software

There are a couple of different options that we use for controlling our 3D printed microscopes, depending on the system. Note: We are not software engineers and so these options may not necessarily be optimal but for now they let us acquire the data that we need for our research.

## Stepper Motor Control

To control the stepper motors connected to the axis actuators on the OpenFlexure stage we use a PiStep2 Quad Stepper Motor Control Board for Raspberry Pi (https://4tronix.co.uk/blog/?p=1309). This is a hat for the Raspberry Pi GPIO pins and allows up to four stepper motors to directly connect to it. We have tested this with a Pi Zero W, Pi 3 Model B+ and Pi 4 Model B. To control the PiStep2 and the motors we have created a simple Python GUI based on Qt and PyQt5. The code can be found in [StepperMotorGUI](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/Control%20Software/StepperMotorGUI). To run the GUI, open and run the file start.py on your Raspberry Pi. The GUI should look like this:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/StepperMotorGUI.png" height=300 width=450>

The default value for the number of steps per click is 50. Altering this will let you control how far the stepper motor turns when you click on the arrow buttons for each axis.

Note: you will need to set up the Pi as outlined [here](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Control%20Software/SingleChannelPiSetup.md) for the code to run.

## Single Channel Brightfield Microscope

To see the details of this microscope please go to [Single Channel Brightfield Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/SingleChannelBrightfield.md).

The core components of this microscope are a basic LED for illumination, an OpenFlexure stage, a 60x finite conjugate objective and a Raspberry Pi Camera Module v2. We have created a simple GUI to control this microscope and take timelapse images on the Raspberry Pi camera. The code for this software can be found in [StepperMotorandLEDGUI](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/Control%20Software/StepperMotorandLEDGUI). Again, to run the GUI, open and run the file start.py on your RaspberryPi. The GUI should look like this:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/StepperMotorandLEDGUI.png" height=600 width=500>

This includes control to switch an LED, which is connected to the PiStep2 hat, on and off. Again, please follow the link to the microscope details above for how to connect this. The same stepper motor control as above is included as well as a section to control the Raspberry Pi Camera. A camera preview can be initiated which allows you to view a live feed whilst controlling the stepper motors. When happy with the position, the camera preview must be stopped before starting a timelapse. To start the timelapse, set the desired camera resolution, the total number of frames required and the interval between each frame. Then select a save directory and click start timelapse. When the timelapse is running a camera preview will also be shown.

Note: you will need to set up the Pi as outlined [here](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Control%20Software/SingleChannelPiSetup.md) for the code to run.

## Multi Channel Microscopes

Multi channel microscopes using multiple Raspberry Pi cameras, such as our [Fluorescence and TIE Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/FluorescenceandTIEMicroscope.md) and [Fluorescence Channel Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/DualFluorescenceMicroscope.md) require more complex software solutions. This is due to the fact that a Raspberry Pi can only connect to and control a single Raspberry Pi camera module. Because of this, if you want to use multiple Pi cameras, you need to use and control multiple Pi's.

Our current method of choice is to use a Raspberry Pi 4 Model B 8gb as a client (controller) Pi. We then connect each camera and the stepper motor hat to separate Pi's (servers) as can be seen in the microscope links above. We connect the client and server Pi's all to the same network. Instructions for connecting to a network can be found here: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

To view the camera previews and control the stepper motors we use VNC (Virtual Network Computing) to remote access the server Pi desktops on the client Pi, so that only the client pi needs to be connected to a monitor, mouse and keyboard. For example in the image below you can see one remote desktop on the client Pi has one of the camera previews and the other has the stepper motor control GUI. You can open multiple remote desktops at once and so can have all the camera previews open. If using v2 camera modules, Pi Zero Ws work for the server Pi's, if using HQ camera modules we recommend using at least Pi 3B+ or optimally Pi 4 8GB. 

To set these Raspberry Pi's up please follow the instructions [here](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Control%20Software/MultiChannelSetup.md).

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/VNCExample.png" height=525 width=900>

Using the remote desktop approach above, you can capture images from individual cameras using Raspicam (https://www.raspberrypi.com/documentation/accessories/camera.html#raspicam-commands) or Picamera (https://picamera.readthedocs.io/en/release-1.13/). This will save images to the individual pi's that the cameras are connected to and you cannot take images simultaneously.

If you would like to capture images "simultaneously" and save the images to the client Pi then the solution we have been using is the Compound Pi project (https://compoundpi.readthedocs.io/en/release-0.4/). Because the Raspberry Pi cameras use a rolling shutter to capture images there is a limitation on how simultaneous capture can actually be along with any possible network delay using the Compound Pi method. However we have achieved simultaneous capture within one tenth of a second using this method (may be more accurate than this but our stopclock at the time had limited precision). Instructions for setting up the Pi's to use Compound Pi can be found [here]
