# Dual Fluorescence Channel Microscope

This section of the FreeCAD file includes designs where we have placed the individual cube designs together to create larger parts for 3D printing. These designs are specifically for parts for a dual fluorescence channel microscope. The wavelength ranges of the detection channels can be chosen by the user by selecting specific dichroic mirrors. In this case we have chosen a 650nm shortpass dichroic mirror and a 490nm shortpass dichroic mirror to create two detection channels, one which detects fluorescence above 650nm and the other which detects fluorescence between 490nm and 650nm.

Note: we are using the new Raspberry Pi HQ cameras in this microscope to capture fluorescence images. These cameras come with an IR filter on them which means if you are trying to image far red fluorescence, the emission will be blocked by the filter. You can follow the instructions [here](https://www.raspberrypi.com/documentation/accessories/camera.html#raspberry-pi-hq-camera-filter-removal) to remove this filter from the camera if using one of these cameras in this detection window.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/DualFluorescenceMicroscope2.png" height=500 width=950>

We have used this microscope in a research project to image mitochondria and bacteria inside human monocyte derived macrophages (samples made by Katharin Balbirnie-Cumming from the Dockrell group at the Centre for Inflammation Research, University of Edinburgh):

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/Macrophages.png" height=425 width=700>

The dual colour image above followed the below processing steps. Image quality will be affected by sample preparation as well as microscope design. As you can see below, the bacteria image had a high background signal which we believe is background labelling and so we have carried out a rolling ball background subtraction for image representation.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/ImageProcessing.png" height=475 width=900>

## Parts to Print

All the STL files needed for this microscope can be found in [Dual Fluorescence Channel Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/STL%20Files/Dual%20Fluorescence%20Channel%20Microscope).

These are the two main cube parts and lids:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/DualFluorescenceMicroscope.png" height=600 width=625>

STL files to print (print settings can be found in the [Cubes](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Cubes.md) and [Inserts](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Inserts.md) build instructions):

* 2x 1 Inch Dichroic Holder
* 2x 1 Inch Lens Holder
* 2x 1 Inch Retaining Ring
* 1x 45 Degree Mirror Holder
* 1x Channel 1
* 1x Channel 2
* 2x Dichroic Locker
* 2x Drop In Filter Holder
* 1x Fluorescence Channel 1 Lid
* 1x Fluorescence Channel 2 Lid
* 1x OpenFlexure Joined to Objective Mount
* 1x OpenFlexure Sample Riser Shortened
* 1x OpenFlexure Stage Adapter Corner Cut Out

Also from the OpenFlexure [website](https://microscope-stls.openflexure.org/#/v6.1.5?enable_smart_brim=true&reflection_illumination=false&optics=rms_f50d13&camera=picamera_2&use_pilens_optics_module=false&riser=sample&microscope_stand%3Abox_h=30&pi_in_base=true&base=bucket&legacy_picamera_tools=false&include_actuator_tension_band=false&include_actuator_drilling_jig=false&motorised=true&use_motor_gears_for_hand_actuation=false) please print the gears, small gears and sample clips STL files.

## Bill of Materials

* Light source:
  * 1x Compact RGB Laser - World Star Tech COMPACT-TS-40-RGB-FC (https://www.worldstartech.com/wp-content/uploads/2017/03/COMPACT-RGB-1.pdf)
  * 1x Thorlabs M42L05 - Ø50 µm, 0.22 NA, Low OH, FC/PC-FC/PC Fiber Patch Cable, 5 m (https://www.thorlabs.com/thorproduct.cfm?partnumber=M42L05)
  * 1x Thorlabs LB1811-A-ML - Mounted N-BK7 Bi-Convex Lens, Ø1", f = 35.0 mm, ARC: 350-700 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=LB1811-A-ML) - for focusing light from fibre onto sample)
  * 1x Thorlabs FESH0650 - Ø25.0 mm Premium Shortpass Filter, Cut-Off Wavelength: 650 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=FESH0650)
* Turning mirror:
  * 1x Thorlabs PF10-03-P01 - Ø1" Protected Silver Mirror (https://www.thorlabs.com/thorproduct.cfm?partnumber=PF10-03-P01)
* Dichroic Mirrors for fluorescence channels:
  * 1x Thorlabs DMSP650 - Ø1" Shortpass Dichroic Mirror, 650 nm Cutoff (https://www.thorlabs.com/thorproduct.cfm?partnumber=DMSP650)
  * 1x Thorlabs DMSP490 - Ø1" Shortpass Dichroic Mirror, 490 nm Cutoff (https://www.thorlabs.com/thorproduct.cfm?partnumber=DMSP490)
* Longpass filters to clean up fluorescence channels:
  * 1x Thorlabs FEL0650 - Ø1" Longpass Filter, Cut-On Wavelength: 650 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=FEL0650)
  * 1x Thorlabs FEL0500 - Ø1" Longpass Filter, Cut-On Wavelength: 500 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=FEL0500)
* Tube lenses:
  * 2x Thorlabs AC254-125-A - f = 125 mm, Ø1" Achromatic Doublet, ARC: 400 - 700 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-125-A) - Tube lens for Fluorescence Channel
* Cameras:
  * 2x Raspberry Pi High Quality Camera (https://www.raspberrypi.org/products/raspberry-pi-high-quality-camera/)
  * 2x CP33/M - SM1-Threaded 30 mm Cage Plate, 0.35" Thick, 2 Retaining Rings, M4 Tap (https://www.thorlabs.com/thorproduct.cfm?partnumber=CP33/M)
  * 2x Thorlabs SM1A9 - Adapter with External C-Mount Threads and Internal SM1 Threads, 4.4 mm Spacer (https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1A9)
  * 2x Thorlabs SM1T2 - SM1 (1.035"-40) Coupler, External Threads, 0.5" Long, Two Locking Rings (https://www.thorlabs.com/thorproduct.cfm?partnumber=SM1T2)
* Objective:
  * 1x Newport LI-60x Microscope Objective Lens, Infinity Corrected, 60x, 0.85 NA, 0.3 mm WD (https://www.newport.com/p/LI-60X) - This objective has been discontinued, this is Newport's new equivalent: https://www.newport.com/p/LIO-60X
* Cage rods:
  * 12x Thorlabs ER6 - Cage Assembly Rod, 6" Long, Ø6 mm (https://www.thorlabs.com/thorproduct.cfm?partnumber=ER6)
  * An equivalent to the Thorlabs rods is to buy lower cost stainless steel 6mm diameter rods. For example we bought 1.5m long rods from RS Components and cut them down to size - https://uk.rs-online.com/web/p/metal-bars-metal-rods/6614680/
* Electronics:
  * 1x Raspberry Pi Zero W (We recommend getting a starter kit, such as https://uk.rs-online.com/web/p/raspberry-pi/1812039/ so that everything you need is included)
  * 3x Raspberry Pi 4 8gb (Again recommend a starter kit https://uk.rs-online.com/web/p/raspberry-pi/2012367)
  * 1x PiStep2 Quad Stepper Controller for Raspberry Pi (https://4tronix.co.uk/blog/?p=1309)
  * 3x 28BYJ-48 5V DC Stepper Motor (https://shop.pimoroni.com/products/5-vdc-stepper-motor-with-uln2003-driver-board)
