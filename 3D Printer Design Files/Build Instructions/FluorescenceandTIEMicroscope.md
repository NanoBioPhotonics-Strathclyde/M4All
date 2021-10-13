# Fluorescence and TIE Microscope

This section of the FreeCAD file includes designs where we have placed the individual cube designs together to create larger parts for 3D printing. These designs are specifically for parts for a multimodal microscope which allows single channel fluorescence imaging and also computational phase imaging based on the transport of intensity equation (TIE). For more information on TIE microscopy please see these papers:

* https://arxiv.org/abs/1707.04139
* https://royalsocietypublishing.org/doi/10.1098/rsos.191921#d3e402

For TIE microscopy, you need to acquire three brightfield images at three different z planes in the sample. Ideally the three planes should be equally spaced apart in z. Our microscope (shown below), which allows TIE images to be acquired, has an infinity corrected objective lens allowing us to create multiple detection channels before focusing the light down onto various cameras. The first channel is a fluorescence channel where, in this case, we excite the sample (such as nanodiamonds) with a 532nm diode laser. Using a 650nm shortpass dichroic allows fluorescence emission above this wavelength to be picked off into the detection channel. The remaining transmitted laser light can then be utilised for TIE imaging. By splitting this light into three channels using beamsplitters, we can offset the tube lenses and focus on three different z planes simultaneously (note: postprocessing for both magnification and xy translation registration may be needed between the channels).

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/TIEMicroscope2.png" height=500 width=1000>

## Parts to Print

All the STL files needed for this microscope can be found in [Fluorescence and TIE Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/3D%20Printer%20Design%20Files/STL%20Files/Fluorescence%20and%20TIE%20Microscope).

These are the two main cube parts:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/TIEMicroscope.png" height=500 width=625>

STL files to print (print settings can be found in the [Cubes](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Cubes.md) and [Inserts](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Inserts.md) build instructions):

* 1x 1 Inch Dichroic Holder
* 4x 1 Inch Lens Holder
* 4x 1 Inch Retaining Ring
* 1x 45 Degree Mirror Holder
* 1x Dichroic Locker
* 4x Drop In Filter Holder
* 1 x Fluorescence Branch
* 1x Fluorescence Channel Lid
* 1x OpenFlexure Joined to Objective Mount
* 1x OpenFlexure Sample Riser Shortened
* 1x OpenFlexure Stage Adapter Corner Cut Out
* 3x Plate Locker
* 3x TIE Branch
* 3x TIE Channel Lid
* 3x Raspberry Pi Camera V2 Holder

Also from the OpenFlexure [website](https://microscope-stls.openflexure.org/#/v6.1.5?enable_smart_brim=true&reflection_illumination=false&optics=rms_f50d13&camera=picamera_2&use_pilens_optics_module=false&riser=sample&microscope_stand%3Abox_h=30&pi_in_base=true&base=bucket&legacy_picamera_tools=false&include_actuator_tension_band=false&include_actuator_drilling_jig=false&motorised=true&use_motor_gears_for_hand_actuation=false) please print the gears, small gears and sample clips STL files.

## Bill of Materials

* Light source:
  * 1x Thorlabs CPS532 Collimated Laser Diode (https://www.thorlabs.com/thorproduct.cfm?partnumber=CPS532)
  * Lens to focus laser down onto sample, such as Thorlabs LB1945-A - N-BK7 Bi-Convex Lens, Ø1", f = 200.0 mm, ARC: 350-700nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=LB1945-A)
* Turning mirror:
  * 1x Thorlabs PF10-03-P01 - Ø1" Protected Silver Mirror (https://www.thorlabs.com/thorproduct.cfm?partnumber=PF10-03-P01)
* Dichroic Mirror for fluorescence channel:
  * 1x Thorlabs DMSP650 - Ø1" Shortpass Dichroic Mirror, 650 nm Cutoff (https://www.thorlabs.com/thorproduct.cfm?partnumber=DMSP650)
* Beamsplitters for brightfield TIE channels:
  * 1x Thorlabs BSS10R - 25 x 36 mm 30:70 (R:T) UVFS Plate Beamsplitter, Coating: 400 - 700 nm, t = 1 mm (https://www.thorlabs.com/thorproduct.cfm?partnumber=BSS10R)
  * 1x Thorlabs BSW10R - 25 x 36 mm 50:50 UVFS Plate Beamsplitter, Coating: 400 - 700 nm, t = 1 mm (https://www.thorlabs.com/thorproduct.cfm?partnumber=BSW10R)
* Second turning mirror:
  * 1x Thorlabs PFR10-P01 - 25 mm x 36 mm Protected Silver Mirror (https://www.thorlabs.com/thorproduct.cfm?partnumber=PFR10-P01)
* ND filters for brightfield TIE channels:
  * 3x Thorlabs ND30B - Unmounted Reflective Ø25 mm ND Filter, Optical Density: 3.0 (https://www.thorlabs.com/thorproduct.cfm?partnumber=ND30B)
* Longpass filter to clean up fluorescence channel:
  * 1x Thorlabs FEL0650 - Ø1" Longpass Filter, Cut-On Wavelength: 650 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=FEL0650)
* Tube lenses:
  * 1x Thorlabs AC254-125-A - f = 125 mm, Ø1" Achromatic Doublet, ARC: 400 - 700 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-125-A) - Tube lens for Fluorescence Channel
  * 3x Thorlabs AC254-045-A - f = 45 mm, Ø1" Achromatic Doublet, ARC: 400 - 700 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-045-A) - Tube lenses for brightfield TIE channels - Due to field distortion and vignetting that occurs when these are used in combination with the Newport LI-40x objective, we now recommend using a longer focal length for the tube lens, such as Thorlabs AC254-100-A - f = 100 mm, Ø1" Achromatic Doublet, ARC: 400 - 700 nm (https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-100-A)
* Cameras:
  * IDS UI-3060CP-M-GL Rev.2 (https://en.ids-imaging.com/store/ui-3060cp-rev-2.html) - Fluorescence channel
  * 3x Raspberry Pi Camera Module v2 (https://www.raspberrypi.org/products/camera-module-v2/) - TIE channels
* Objective:
  * 1x Newport LI-40x Microscope Objective Lens, Infinity Corrected, 40x, 0.65 NA, 0.36 mm WD (https://www.newport.com/p/LI-40X) - This objective has been discontinued, this is Newport's new equivalent: https://www.newport.com/p/LIO-40X
* Cage rods:
  * 10x Thorlabs ER4 - Cage Assembly Rod, 4" Long, Ø6 mm (https://www.thorlabs.com/thorproduct.cfm?partnumber=ER4)
  * 4x Thorlabs ER6 - Cage Assembly Rod, 6" Long, Ø6 mm (https://www.thorlabs.com/thorproduct.cfm?partnumber=ER6)
  * An equivalent to the Thorlabs rods is to buy lower cost stainless steel 6mm diameter rods. For example we bought 1.5m long rods from RS Components and cut them down to size - https://uk.rs-online.com/web/p/metal-bars-metal-rods/6614680/
* Electronics:
  * 4x Raspberry Pi Zero W (We recommend getting a starter kit, such as https://uk.rs-online.com/web/p/raspberry-pi/1812039/ so that everything you need is included)
  * 1x Raspberry Pi 4 8gb (Again recommend a starter kit https://uk.rs-online.com/web/p/raspberry-pi/2012367)
  * 3x Raspberry Pi Camera Cable - Raspberry Pi Zero edition (https://shop.pimoroni.com/products/camera-cable-raspberry-pi-zero-edition?variant=32092803891283)
  * 1x PiStep2 Quad Stepper Controller for Raspberry Pi (https://4tronix.co.uk/blog/?p=1309)
  * 3x 28BYJ-48 5V DC Stepper Motor (https://shop.pimoroni.com/products/5-vdc-stepper-motor-with-uln2003-driver-board)




