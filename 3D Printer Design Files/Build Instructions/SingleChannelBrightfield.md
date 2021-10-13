# Single Channel Brightfield Microscope

This section of the FreeCAD file includes designs where we have placed the individual cube designs together to create larger parts for 3D printing. These designs are specifically for parts for a single channel brightfield microscope. This microscope includes a low cost LED which can be controlled using the PiStep2 stepper motor hat for a Raspberry Pi, a finite conjugate objective and a Raspberry Pi v2 camera. If you wanted you could also swap the finite conjugate objective for an infinity corrected one and then add a tube lens between the objective and camera using on of our lens inserts.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/SingleChannelBrightfield2.png" height=500 width=425>

The PiStep2 motor control board has 4 stepper motor connectors. On each of these connectors there is one ground pin and 4 pins which connect to the Raspberry Pi GPIO pins. As we only need to use three stepper motors for the OpenFlexure stage, there is one spare. This spare one can be used to connect to the LED to control it via GPIO. Using jumper cables connect the cathode of the LED to the ground pin and the anode to one of the other pins on the connector, as shown in the above photo. You should also connect a resistor between the anode and the connector pin. The ground pin on the connector is the one which is not connected to an indicator LED.

## Parts to Print

All the STL files for this microscope can be found in [Single Channel Brightfield](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/3D%20Printer%20Design%20Files/STL%20Files/Single%20Channel%20Brightfield).

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/SingleChannelBrightfield.png" height=500 width=550>

STL files to print (print settings can be found in the [Cubes](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Cubes.md) and [Inserts](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Inserts.md) build instructions):

* 1x Single Channel Brightfield
* 1x Single Channel Brightfield Lid
* 1x OpenFlexure Joined to Objective Mount
* 1x OpenFlexure Sample Riser Shortened
* 1x OpenFlexure Stage Adapter
* 1x Raspberry Pi Camera V2 Holder

Also from the OpenFlexure [website](https://microscope-stls.openflexure.org/#/v6.1.5?enable_smart_brim=true&reflection_illumination=false&optics=rms_f50d13&camera=picamera_2&use_pilens_optics_module=false&riser=sample&microscope_stand%3Abox_h=30&pi_in_base=true&base=bucket&legacy_picamera_tools=false&include_actuator_tension_band=false&include_actuator_drilling_jig=false&motorised=true&use_motor_gears_for_hand_actuation=false) please print the gears, small gears, sample clips, condenser and illumination dovetail.
