# OpenFlexure Options

We needed to make a couple of modifications to the OpenFlexure stage for it to be compatible with our modular system. The first is the objective mount was too long and wouldn't allow a turning mirror to sit underneath the stage in one of our cubes, so we altered the objective mount to make it shorter. The second was we encountered problems with tilt of the objective mount when screwing it onto the stage, therefore we combined the designs for the stage and the objective mount to print them together monolithically. We think this wasn't a fault of the stage design but a fault in the calibration of our 3D printer, commonly known as "[elephant foot](https://all3dp.com/2/elephant-s-foot-3d-printing-problem-easy-fixes/)". By making these two parts monolithic we avoid the need to worry about this calibration error.

These parts were printed with the settings recommended by OpenFlexure (https://build.openflexure.org/openflexure-microscope/v6.1.5/docs/#/0_printing).

# Altered OpenFlexure RMS Objective Mount

We imported the STL file for the OpenFlexure Objective mount (named "optics_picamera_2_rms_f50d13.stl" from https://openflexure.org/projects/microscope/build) into FreeCAD and edited it following the instructions found here for editing STL files in FreeCAD - https://all3dp.com/1/7-free-stl-editors-edit-repair-stl-files/. All we did was cut the bottom of the mount off in FreeCAD to make it shorter.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/OpenFlexureObjectiveMount.png" height=300 width=800>

# OpenFlexure Stage Option

To join the designs of the above objective mount together with the OpenFlexure Stage, we imported the STL file for the desired OpenFlexure stage into FreeCAD, then duplicated the objective mount design and moved it so that it was flush with the stage design. We added both these files to a "part" in FreeCAD and then exported the part as an STL file. We then also edited the OpenFlexure sample riser (named sample_riser_LS10.stl from https://openflexure.org/projects/microscope/build) using the same process as for the objective mount to shorten it for our specific objective. This is needed because the position of the objective mount is now fixed. The objective this is designed for is the Newport LI-60x (https://www.newport.com/p/LI-60X). This objective is no longer available however it has a standard parfocal length of 45mm and so this stage option should be compatible with other 45mm parfocal RMS threaded objectives.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/OpenFlexureStageOptions.png" height=450 width=600>
