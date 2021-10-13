# Setting Up Compound Pi to Control Multiple Pi's

## Setting Up the Client

Firstly set up the client Raspberry Pi (recommended to use a Raspberry Pi 4 Model B 8gb), connect to a monitor, keyboard and mouse and install Raspberry Pi OS (32-bit) according to the instructions on the official Raspberry Pi website (https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/0).

Connect to a network following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

If it's not already installed then download VNC viewer from: https://www.realvnc.com/en/connect/download/viewer/raspberrypi/

Open a terminal and install the following:

* sudo apt-get update
* sudo apt-get install compoundpi-client ntp

Reboot the Pi.

Set a static IP address. To do this edit the dhcpcd file by typing sudo nano /etc/dhcpcd.conf into the terminal. Go down to the bottom and uncomment the below lines and change them to:
	
interface wlan0

static ip_address=192.168.0.10/24 

static routers=192.168.0.1

static domain_name_servers=192.168.0.1

Reboot the Pi.

## Setting Up the Servers

Note: these instructions are only for server Pi's connected to cameras. For the server connected to the stepper motors please follow the server setup [here](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Control%20Software/MultiChannelSetup.md).

You can shut down and disconnect the power from the client Pi that you have already connected to a monitor etc. Then you can swap to a fresh SD card to set up a server Pi (keeping the client SD card in a safe place in the mean time). Or you can connect your server Pi to a monitor etc.

Again install Raspberry Pi OS (32-bit) according to the instructions on the official Raspberry Pi website (https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/0).

Connect to a network following these instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-using/3#:~:text=If%20you%20want%20to%20connect,connect%20to%20a%20wireless%20network.

To enable VNC follow step 1 here: https://magpi.raspberrypi.com/articles/vnc-raspberry-pi

Then open up VNC server, go to Options > Troubleshooting and check "Enable direct capture mode" and apply and click ok.

Open a terminal and install:

* sudo apt-get install compoundpi-server ntp

Set a static IP address. To do this edit the dhcpcd file by typing sudo nano /etc/dhcpcd.conf into the terminal. Go down to the bottom and uncomment the below lines and change them to:
	
interface wlan0

static ip_address=192.168.0.11/24         (Note: for each Pi change to 192.168.0.12/24, 192.168.0.13/24 etc.)

static routers=192.168.0.1

static domain_name_servers=192.168.0.1

Reboot the Pi.

Edit the /etc/ntp.conf file and replace the server lines with the IP address of your client:

...

#server 0.debian.pool.ntp.org iburst

#server 1.debian.pool.ntp.org iburst

#server 2.debian.pool.ntp.org iburst

#server 3.debian.pool.ntp.org iburst

server 192.168.1.2

...

Restart the NTP daemon:

* sudo service ntp restart

Reboot the Pi.

## Using Compound Pi and VNC

Compound Pi allows the simultaneous capture (within limits) of images from different Raspberry Pi cameras connected to different Raspberry Pi's. However, it does not offer a method of previewing the camera streams before. Therefore, we use this in combination with remote desktops through VNC to preview cameras. With all of the prepared SD cards in their respective Pi's, and the Pi's booted, open the server Pi's on VNC viewer on the client using the static IP addresses that you assigned them. On the remote desktop for each server that you would like to view the camera open a terminal and type in:

* sudo service cpid stop

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/cpidstop.png" height=500 width=900>

Once you have done this you will be able to either use Raspicam or Picamera to view the camera preview on the remote desktop. This will allow you to get your sample into position and focus etc. Then once you are happy and would like to capture images, open the terminal again and type:

* sudo service cpid start

After this, minimise the remote desktops on the client and open a terminal on the client and type:

* cpi

This will start the compoundpi client.

Then type:

* set network 192.168.0.1/24
* set timeout 400
* find n (where n is the number of server pi's you want to capture from or you can add a specific server by typing add 192.168.0.11 etc.)
* resolution 3280x2462
* framerate 30
* iso 200
* exposure 50
* set output /home/pi/
* capture
* download

You can change the camera settings above and set the output to a folder on the client where you want the images to save to. When you type capture, the servers all capture an image on their Pi camera and then download pulls them over to the client. When you download them it also clears the images from the servers.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/cpi.png" height=500 width=900>

