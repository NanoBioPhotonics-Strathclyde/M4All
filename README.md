# M4All: MultiModal Modular Microscopy for All
[![DOI](https://zenodo.org/badge/379953786.svg)](https://zenodo.org/badge/latestdoi/379953786)

M4All is a modular 3D printable microscopy system which allows users to design setups for different imaging modalities (can also be used for non-imaging optical systems). The project is led by Gemma Cairns as part of her PhD in the NanoBioPhotonics group at the University of Strathclyde. Other significant contributers from the group are Brian Patton and past member Stephen Grant.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/Overview.png" height=550 width=800>

There are multiple approaches for open microscopy hardware, for example see the project list at https://github.com/HohlbeinLab/OpenMicroscopy, and we recommend trying a few and choosing a project based on what your aims are. When designing this system we approached it from the view point of requiring light tight and stable setups which would allow us to implement and test cutting edge microscopy techniques on a budget. As such M4All is best suited to those with prior microscopy experience or those working with people with similar optical experience. We are confident that M4All systems allow us to generate publication quality images and results.

M4All is based on modular cubes which include 6mm rod holes compatible with standard 30mm cage system optomechanics (multiple manufacturers make compatible components). There are various challenges when it comes to 3D printing, especially when the aim is to create accurate structures for imaging devices. There are often discrepancies between different 3D printers and their printing tolerances. Even small defects in printed parts can be enough to cause problems when trying to join different parts together, which in turn can lead to alignment and stability problems in 3D printed imaging systems. To try and address this problem, our approach is to provide a package of modular cube design files which can be joined together to create larger parts prior to printing to improve stability. By printing larger parts, or ideally the microscope as one single body if printing dimensions allow, this reduces the number of errors that can build up when printing individual modular cubes, although at the expense of decreased flexibility post printing. Note that this approach should not change the total printing time.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/BaseCubeDiagram.PNG" height=375 width=700>

You can see the base cube design above with the cage system highlighted. The cubes also have M6 screw holes on the bottom to allow securing parts onto an optical bench or other surface and to hold larger parts together in the system. We have included a jigsaw system on the top of the cubes as well to attach corresponding light tight lids or attachments for other parts, such as one we have designed to allow the OpenFlexure Microscope (https://openflexure.org/projects/microscope/) to be compatible with our system. On the topic of keeping imaging systems light tight, we have also provided an array of base cube designs with different walls cut out and including the cage system so that users can design their microscope with the outer walls closed. For alternatives to commercial optomechanics we have also provided designs for 3D printed parts compatible with this system to hold various different optics, such as lenses, mirrors, beamsplitters, dichroics and raspberry pi cameras.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/InsertsDiagram.png" height=400 width=600>

To address the differences in printing tolerances between different 3D printers, we also provide test pieces which users can print to optimise both design dimensions and printer settings. For example the two test pieces shown below allow you to determine which radius to set the 6mm rod holes as in the CAD files so that they aren't too large or small when printing the cubes and inserts. Tolerances also vary for printing in either the xy or z planes and so this is why there are two test piece orientations.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/TestPieceDiagram.png" height=400 width=600>

## Applications

We have used this system to design and build multiple different microscopes.

The first is a [Single Channel Brightfield Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/SingleChannelBrightfield.md). We recommend new users to our system build one of these first to understand our approach and calibrate their 3D printer for our designs.

The next is a [Fluorescence and TIE Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/FluorescenceandTIEMicroscope.md) which shows the level of complexity that can be successfully implemented with our designs:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/TIEMicroscope2.png" height=425 width=800>

The third is a [Dual Fluorescence Channel Microscope](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/DualFluorescenceMicroscope.md). This microscope takes fluorescence images with the latest Raspberry Pi HQ cameras.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/DualFluorescenceMicroscope2.png" height=450 width=800>

We have successfully used this microscope in a research project to acquire images of bacteria and mitochondria in human monocyte derived macrophages:

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/Images/Macrophages.png" height=425 width=700>

## Design Files and Build Instructions

All of our designs are produced using the open source CAD software FreeCAD (https://www.freecadweb.org/).

Note: We used FreeCAD version 0.18 which can be found here https://github.com/FreeCAD/FreeCAD/releases if there are any compatibility issues with newer releases.

For FreeCAD and STL design files please see the [3D Printer Design Files](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files) folder.
This section also includes build instructions.

Note: We have also included modified designs from the OpenFlexure project (https://openflexure.org/projects/microscope/). Original designs and modifications are detailed in the design folders in accordance with the CERN Open Hardware Licence.

## Control Software

For microscope control software please see [Control Software](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/Control%20Software). 

Note: We are not software engineers and so these options may not necessarily be optimal but for now they let us acquire the data that we need for our research.

## Multi Channel Alignment and Calibration Tools

Coming soon...

## Licence

Our hardware designs are licenced under the CERN Open Hardware Licence Version 2 (CERN-OHL-S).

Our software is licenced under the GNU General Public License v3.0.
