# Setting Up VNC to Control Multiple Pi's

## Setting Up the Client

Firstly set up the client Raspberry Pi (recommended to use a Raspberry Pi 4 Model B 8gb), connect to a monitor, keyboard and mouse and install Raspberry Pi OS (32-bit) according to the instructions on the official Raspberry Pi website (https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/0).

The OS doesn't use Python 3 by default and so follow the instructions here to use Python 3 and install pip: https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all

Connect to a network following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

If it's not already installed then download VNC viewer from: https://www.realvnc.com/en/connect/download/viewer/raspberrypi/

## Setting Up the Servers

To do this you can shut down and disconnect the power from the client Pi that you have already connected to a monitor etc. Then you can swap to a fresh SD card to set up a server Pi (keeping the client SD card in a safe place in the mean time). Or you can connect your server Pi to a monitor etc.

Again install Raspberry Pi OS (32-bit) according to the instructions on the official Raspberry Pi website (https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/0).

Connect to a network following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

The OS doesn't use Python 3 by default and so follow the instructions here to use Python 3 and install pip: https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi/all

Now open a terminal on the Raspberry Pi and install the following:

* PyQt5: sudo apt-get install python3-pyqt5
* qt5-default: sudo apt-get install qt5-default
* qtcreator: sudo apt-get install qtcreator
* OpenCV: pip install opencv-contrib-python

All other packages such as numpy, RPi.GPIO, threading etc. should already be installed with Raspberry Pi OS.

For the server Pi that will be used to control the stage stepper motors also save a copy of the [StepperMotorGUI](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/Control%20Software/StepperMotorGUI) to the Pi.

To enable VNC follow step 1 here: https://magpi.raspberrypi.com/articles/vnc-raspberry-pi

Then open up VNC server, go to Options > Troubleshooting and check "Enable direct capture mode" and apply and click ok.

Also when you open VNC server note down the IP address that has been assigned to the Pi to use in VNC viewer. Or you also have the option to set a static IP address. To do this edit the dhcpcd file by typing sudo nano /etc/dhcpcd.conf into the terminal. Go down to the bottom and uncomment the below lines and change them to:
	
interface wlan0
static ip_address=192.168.0.10/24 
static routers=192.168.0.1
static domain_name_servers=192.168.0.1

For the static ip_address above you can set different server Pi's to 192.168.0.11/24, 192.168.0.12/24, 192.168.0.13/24 etc.

You can either repeat this process for all the server Pi SD cards or you can clone one that has already been set up via this [method](https://www.howtogeek.com/341944/how-to-clone-your-raspberry-pi-sd-card-for-foolproof-backup/). However, you will then need to find all their IP addresses for example using an IP scanner https://learn.pimoroni.com/article/finding-your-raspberry-pi or after cloning manually changing their static IP address.

Once all the SD cards are set up then they can be inserted into the relevant Pi's connected to a camera or stepper motor hat and the client SD card can be inserted back into the client Pi. Upon powering on all the Pi's they should connect automatically to the network which was selected during set up.

If VNC viewer on the client Pi cannot connect to a certain IP address then it may be that the server hasn't in fact conected to the network upon boot. If this happens, which we have come across when using a Pi 4 as a server, then follow the below instructions:

Plug the server SD card into a windows computer. To the boot partition create a blank file using notebook and save it as ssh. Don't save it with a file extension. Then also create a file called wpa_supplicant.conf with the following wifi network info (changing the ssid and psk to your network info):

country=GB
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="NETWORK-NAME"
    psk="NETWORK-PASSWORD"
}

Once done, replace the SD card back into the server pi and boot.

Then on your controller pi which is connected to the same network open a terminal and type in:

ssh pi@192.168.0.16 

Replace the IP address above with whatever the IP address for the server Pi is.

Then you can put in the password and the pi should boot.

Now you should be able to open the pi using vnc viewer.
