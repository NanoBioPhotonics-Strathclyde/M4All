# Build Instructions

Original FreeCAD design files are in the [FreeCAD Files](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/3D%20Printer%20Design%20Files/FreeCAD%20Files) folder.

STL files for 3D printing can be found in the [STL Files](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/3D%20Printer%20Design%20Files/STL%20Files) folder.

## FreeCAD Instructions

Upon opening the FreeCAD file named "Designs" you will see that the designs are all grouped into different areas (further information on these can be found in [Build Instructions](https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/tree/main/3D%20Printer%20Design%20Files/Build%20Instructions):

* **Basic Cubes** are the basic building blocks of the modular system. Included are various cube designs with different numbers of sides cut out for joining together in different orientations for the optical system that the user requires. The cubes have screw holes in the bottom to allow them to be screwed onto an optical table, using M6 screws, for stability and to lock separate parts together. The cubes have 6mm rod holes compatible with 30mm cage system optomechanics.
* **Open Ended Cubes** are similar to the basic cubes but have entire walls cut out for creating extended cubes where maybe a wall would be at a position where you would like an optical element to be placed.
* **Cube Lids** are screwless lids that fix onto the top of the cubes using a jigsaw system to allow a light tight optical setup. 
* **25mm x 36mm Beamsplitter Cubes** include three different options for specifically holding 25mm x 36mm plate beamsplitters/dichroics/ mirrors (more details below).
* **Inserts** includes design files for holding different optical elements using the 30mm cage system. So far these include:
  * a 45 degree 1 inch mirror holder
  * a 1 inch plate dichroic holder with plate to lock dichoic in place.
  * a 1 inch lens holder with retaining ring
  * a Raspberry Pi Camera v2 holder
  * a drop in 1 inch filter holder
* **Raspberry Pi Holders** includes raspberry pi cases that can be screwed onto an optical table for stability.
* **OpenFlexure Stage Adapter** is an adapter plate for the OpenFlexure microscope, using the same jigsaw system as the cube lids, to allow the OpenFlexure xyz stage to be used.
* **Test Pieces** allow users to find the best settings and design dimensions for their specific 3D printers before printing full designs.
* **Fluorescence and TIE Microscope** includes larger recommended parts made up of the modular cubes for a multimodal microscope setup including fluorescence and computational phase contrast imaging.
* **Dual Fluorescence Channel Microscope** again includes larger recommended parts for a dual channel fluorescence microscope.

### Test Pieces

As the tolerances of different models of 3D printers and different 3D printing materials vary, it is recommended to print the test parts provided to optimise print settings and design dimensions. 

1. **Rod Hole Test Piece Vertical** allows users to test what rod hole radius to use for the cube walls and any inserts or parts where the print orientation means the rod hole is on a vertical wall. The test piece includes rod hole radii ranging from 3-3.25mm. Three vertical walls are included in the test piece so users can check the 6mm metal rods go through multiple walls. Note: you want there to be enough friction that the rods don't slide about but not too much friction so that the rods can't easily go through multiple walls.
2. **Rod Hole Test Piece Horizontal** includes two test pieces for testing what rod hole radius to use for any inserts or parts where the print orientation means the rod hole is on a horizontal wall. They cover radii from 3-3.55mm.

The user can test these parts with different print settings, such as varying layer height and infill, for optimisation.

### Altering Design Dimensions Based on Test Pieces

Once you have determined what rod hole radius to use based on the test pieces, you can then alter the FreeCAD designs accordingly, if needed.

FreeCAD is a parametric 3D CAD modeler, meaning 2D sketches are turned into 3D objects using constraints. Therefore the rod hole sketches can be easily altered by changing the radius constraint in the 2D sketch as shown below.

1. Select the necessary body from the tree view and expand. 
2. Find the rod hole sketches. There will be one for each cube wall.
3. Open up the sketch.
4. Alter the radius contraints to the required value.

Note: Currently this needs to be done manually for all sketches and bodies/parts.

![](https://github.com/gemmacairns/3D-Printed-Microscopes/blob/master/3D%20Printer%20Design%20Files/Instruction%20Clips/EditRodHoleRadius.gif)

### Joining Cube Designs Together

The modularity of the M<sup>4</sup> system comes from modular design files which can be joined together before printing to create stable larger parts. Each 50x50mm cube has M6 screw holes on the bottom for fixing to an optical table, jigsaw lid system and 6mm metal rod holes for a 30mm cage system. By joining different cube designs together, users can create suitable parts for their optical systems. The clip below shows how to join two cubes together. 

1. From the tree menu on the left hand side, duplicate the required cubes (FreeCAD Body) using Ctrl+C and Ctrl+V either into the same FreeCad file or a new file. The duplicates will be in the same position as the original bodies.
2. To move the position of the cubes, click on the body in the tree view and alter the x and y positions. As the cubes are 50x50mm, offsetting them in 50mm increments will allow the walls to be joined with the cut outs and rod holes aligning with each other.
3. If step 3 was done correctly, when you export to an stl file the cubes will be fused together and print as one with no joins evident. 
4. To export to an stl file for 3D printing you can either select the two bodies and go to File>Export and save as a .stl, or you can create a Part in FreeCad and add the two bodies (cubes) to the Part. This is useful if creating a part with many body files. You can then simply select the Part in the tree view and again go to File>Export and save as a .stl file (as in the clip below).

Parts in the "Fluorescence and TIE Microscope" and "Dual Fluorescence Channel Microscope" groups were created using this process.

Individual cube lids can also be joined together in this way to create monolithically printed lids to cover your specific cube designs. 

![](https://github.com/gemmacairns/3D-Printed-Microscopes/blob/master/3D%20Printer%20Design%20Files/Instruction%20Clips/HowToJoinCubes.gif)

### 25mm x 36mm Beamsplitter Cubes

You will notice that there are three different options for cubes to specifically hold 25mm x 36mm optics such as plate beamsplitters and dichroics. The size of these optical parts mean they are not compatible with the 30mm cage system and so we have designed specific cubes for this purpose.

Note: The current designs are to hold a plate thickness of 1mm, but this can be altered in FreeCAD.

1. **Beamsplitter Cube** has a plate holder that is monolithically printed inside the cube. Two bars can then be screwed in place using M3 screws to hold the optic in place. As the screws need to be screwed in through the holes in the cube walls, this part is only suitable if printed as a single cube and not joined to others where these walls would be blocked.
2. **Beamsplitter Cube001** is similar to the first option, however this design includes a plate locker that slides into two gaps on the bottom of the cube and screws onto the top of the plate. Therefore this cube can be joined to others and printed monolithically.
3. **Beamsplitter Cube002** has the plate holder separate from the cube. The cube includes a section where the plate holder can be inserted into and the same bars as in the first option are included for holding the optic in place.

It is recommended to print these with either support material or if using Cura to enable bridge settings. I have uploaded the settings file used for our Ultimaker S5 here...

For option 2, if you find that your optical element is not sitting completely vertical (e.g. if there is an angle to the reflected and transmitted beams), you can add shims to the inside of the plate locker by adding layers of electrical tape to either the top or bottom.

Option 3 has not yet been fully tested.

### Inserts

The orientation of the inserts in FreeCAD are the recommended printing orientation. Again the test pieces can be used to determine which rod hole radius to use.

1. **45 Degree Mirror Holder** has been designed to hold a 1 inch mirror with thickness 6mm at 45 degrees. This can be hung from the cage system rods two different ways. The first orientation is to reflect a beam coming vertically down into cubes by 45 degrees so that it can travel horizontally around the cube system. This is useful for sample stages that sit above the cubes. The second orientation allows beams to be turned inside the cube system.
2. **1 Inch Dichroic Holder** is similar to the mirror holder however it has channels to allow the transmitted beam to pass through the insert. It has been designed for a dichroic thickness of 3mm. There is also a plate to lock the dichroic in place with M3 screws.
3. **Raspberry Pi Camera v2 holder** has a slight indent for the camera module to fit into with a gap at the back for space for the electronics. There are 4 screw holes to hold the camera module in place with nuts at the back. The insert also has a cut out at the top for the camera cable. On the top of the insert there are self tapping M3 screw holes to provide some friction between the insert and the rods to hold it in place.
4. **1 Inch Lens Holder** will fit various thicknesses of 1 inch lenses which can be held in place with the retaining ring design. If a greater thickness is required the FreeCAD design can be modified. The top of the insert again has screw holes to hole the insert in place on the metal rods.

