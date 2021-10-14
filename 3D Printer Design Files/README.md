# Build Instructions

Original FreeCAD design files are in the [FreeCAD Files](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/FreeCAD%20Files) folder.

Note: We used FreeCAD version 0.18 which can be found here https://github.com/FreeCAD/FreeCAD/releases if there are any compatibility issues with newer releases.

STL files for 3D printing can be found in the [STL Files](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/STL%20Files) folder.

## FreeCAD Instructions

Upon opening the FreeCAD file named "Designs", found [here](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/FreeCAD%20Files), you will see that the designs are all grouped into different areas. Below is a brief overview of our design groups with further information found in [Build Instructions](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/Build%20Instructions)). Each section in the build instructions has print settings recommended for each part and we also include details of three different microscopes we have built using the M4All system.

Once you have familiarised yourself with our designs we recommend following steps 1 and 2 below to optimise designs/calibrate print settings. We recommend optimising a single cube before printing larger systems. Once happy with this you can either print the parts for one of the three microscopes we describe below (we recommend starting with the single channel brightfield microscope), or you can create your own cube systems using the instructions in step 3 below.

* [**Cubes**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Cubes.md):
  * **Basic Cubes** are the basic building blocks of the modular system. Included are various cube designs with different numbers of sides cut out for joining together in different orientations for the optical system that the user requires. The cubes have screw holes in the bottom to allow them to be screwed onto an optical table, using M6 screws, for stability and to lock separate parts together. The cubes have 6mm rod holes compatible with 30mm cage system optomechanics.
  * **Open Ended Cubes** are similar to the basic cubes but have entire walls cut out for creating extended cubes where maybe a wall would be at a position where you would like an optical element to be placed. 
  * **25mm x 36mm Beamsplitter Cubes** include three different options for specifically holding 25mm x 36mm plate beamsplitters/dichroics/ mirrors.
  * **Cube Lids** are screwless lids that fix onto the top of the cubes using a jigsaw system to allow a light tight optical setup.
* [**Inserts**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/Inserts.md) includes design files for holding different optical elements using the 30mm cage system. So far these include:
  * a 45 degree 1 inch mirror holder
  * a 1 inch plate dichroic holder with plate to lock dichoic in place.
  * a 1 inch lens holder with retaining ring
  * a Raspberry Pi Camera v2 holder
  * a drop in 1 inch filter holder
* [**Raspberry Pi Holders**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/RaspberryPiHolders.md) includes raspberry pi cases that can be screwed onto an optical table for stability.
* [**OpenFlexure Stage Adapter**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/OpenFlexureStageAdapter.md) is an adapter plate for the OpenFlexure microscope, using the same jigsaw system as the cube lids, to allow the OpenFlexure xyz stage to be used.
* **Test Pieces** allow users to find the best settings and design dimensions for their specific 3D printers before printing full designs.
* [**Single Channel Brightfield Microscope**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/SingleChannelBrightfield.md) includes larger parts recommended to build a simple single channel brightfield microscope. We recommend building one of these first if new to our system in order to understand our approach and calibrate your 3D printer for our designs.
* [**Fluorescence and TIE Microscope**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/FluorescenceandTIEMicroscope.md) includes larger recommended parts made up of the modular cubes for a multimodal microscope setup including fluorescence and computational phase contrast imaging.
* [**Dual Fluorescence Channel Microscope**](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Build%20Instructions/DualFluorescenceMicroscope.md) again includes larger recommended parts for a dual channel fluorescence microscope.

### Step 1: Test Pieces

As the tolerances of different models of 3D printers and different 3D printing materials vary, it is recommended to print the test parts provided [here](https://github.com/NanoBioPhotonics-Strathclyde/M4All/tree/main/3D%20Printer%20Design%20Files/STL%20Files/Test%20Pieces) to optimise print settings and design dimensions. Tolerances also vary for printing in either the xy or z planes and so this is why there are two test piece orientations.

1. **Rod Hole Test Piece Vertical** allows users to test what rod hole radius to use for the cube walls and any inserts or parts where the print orientation means the rod hole is on a vertical wall. The test piece includes rod hole radii ranging from 3-3.25mm. Three vertical walls are included in the test piece so users can check the 6mm metal rods go through multiple walls. Note: you want there to be enough friction that the rods don't slide about but not too much friction so that the rods can't easily go through multiple walls.
2. **Rod Hole Test Piece Horizontal** includes two test pieces for testing what rod hole radius to use for any inserts or parts where the print orientation means the rod hole is on a horizontal wall. They cover radii from 3-3.55mm.

The user can test these parts with different print settings, such as varying layer height and infill, for optimisation.

We don't currently have test pieces for optimising inserts. However in the build instructions we detail how to alter important dimensions in case you need to change these for your printer or optics. We suggest starting off with the recommended print settings and adjusting appropriately there after.

### Step 2: Altering Design Dimensions Based on Test Pieces

Once you have determined what rod hole radius to use based on the test pieces, you can then alter the FreeCAD designs accordingly, if needed.

FreeCAD is a parametric 3D CAD modeler, meaning 2D sketches are turned into 3D objects using constraints. Therefore the rod hole sketches can be easily altered by changing the radius constraint in the 2D sketch as shown below.

1. Select the necessary body from the tree view and expand. 
2. Find the rod hole sketches. There will be one for each cube wall.
3. Open up the sketch.
4. Alter the radius contraints to the required value.

Note: Currently this needs to be done manually for all sketches and bodies/parts.

![](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Instruction%20Clips/EditRodHoleRadius.gif)

### Step 3: Joining Cube Designs Together

The modularity of the M4All system comes from modular design files which can be joined together before printing to create stable larger parts. Each 50x50mm cube has M6 screw holes on the bottom for fixing to an optical table, jigsaw lid system and 6mm metal rod holes for a 30mm cage system. By joining different cube designs together, users can create suitable parts for their optical systems. The clip below shows how to join two cubes together. 

1. From the tree menu on the left hand side, duplicate the required cubes (FreeCAD Body) using Ctrl+C and Ctrl+V either into the same FreeCad file or a new file. The duplicates will be in the same position as the original bodies.
2. To move the position of the cubes, click on the body in the tree view and alter the x and y positions. As the cubes are 50x50mm, offsetting them in 50mm increments will allow the walls to be joined with the cut outs and rod holes aligning with each other.
3. If step 3 was done correctly, when you export to an stl file the cubes will be fused together and print as one with no joins evident. 
4. To export to an stl file for 3D printing you can either select the two bodies and go to File>Export and save as a .stl, or you can create a Part in FreeCad and add the two bodies (cubes) to the Part. This is useful if creating a part with many body files. You can then simply select the Part in the tree view and again go to File>Export and save as a .stl file (as in the clip below).

Parts in the "Fluorescence and TIE Microscope" and "Dual Fluorescence Channel Microscope" groups were created using this process.

Individual cube lids can also be joined together in this way to create monolithically printed lids to cover your specific cube designs. 

![](https://github.com/NanoBioPhotonics-Strathclyde/M4All/blob/main/3D%20Printer%20Design%20Files/Instruction%20Clips/HowToJoinCubes.gif)



