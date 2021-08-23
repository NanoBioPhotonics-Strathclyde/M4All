# Inserts

The orientation of the inserts in FreeCAD are the recommended printing orientation, with the exception of the Dichroic Locker - this will need laid flat in your 3D printing software before printing. 

The only two that require to be printed with support material are the 45 Degree Mirror Holder and the 1 Inch Dichroic Holder. For the 45 Degree Mirror Holder you can either use PLA as the support material or specific support material like PVA. For the 1 Inch Dichroic Holder it needs to be dissolvable support material like PVA.

We print these on an Ultimaker S5 using 0.2mm layer height and 50% infill on Cura. You can increase the infill for increased strength and you can also reduce the layer height for greater accuracy. So far we have only printed these in standared Ultimaker PLA.

## 45 Degree Mirror Holder

This part holds a 1 inch mirror with thickness 6mm at 45 degrees. This can be hung from the cage system rods in two different orientations. The first orientation is to reflect a beam coming vertically down into cubes by 45 degrees so that it can travel horizontally around the cube system. This is useful for sample stages that sit above the cubes. The second orientation allows beams to be turned inside the cube system.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/45DegreeMirrorHolder.png" height=300 width=300>

The radius and thickness of the cylinder to hold the mirror can be altered in FreeCAD if different sized mirrors are required. Expanding the "Inserts" folder in the tree view on FreeCAD will then allow you to expand the body design "45 Degree Mirror Holder". Editing the "Mirror Hole" sketch will allow you to alter the radius. Editing the "Mirror Hole Pocket" will allow you to alter the thickness.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/EditMirrorHolder.png" height=525 width=700>

## 1 Inch Dichroic Holder

This part is similar to the mirror holder however it has channels to allow the transmitted beam to pass through the insert. It has been designed for a dichroic thickness of 3mm. There is also a plate to lock the dichroic in place with M3 screws. This part can also be used for 1 inch beamsplitters.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/1InchDichroicHolder.png" height=300 width=500>

Again the dimensions of the part can be altered in FreeCAD if different sized optics are required in the same way as above.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/EditDichroicHolder.png" height=525 width=700>

## Raspberry Pi Camera v2 Holder

This part has a slight indent for the camera module to fit into with a gap at the back for space for the electronics. There are 4 screw holes to hold the camera module in place with nuts at the back. The insert also has a cut out at the top for the camera cable. On the top of the insert there are self tapping M3 screw holes to provide some friction between the insert and the rods to hold it in place.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/PiCameraV2Holder.png" height=300 width=300>

## 1 Inch Lens Holder

This part is designed to hold a 1 inch lens or filter which can be held in place with the retaining ring design. The top of the insert again has M3 screw holes to hold the insert in place on the metal rods. 

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/1InchLensHolder.png" height=300 width=300>

If a greater thickness is required to hold thicker optics the FreeCAD design can be modified by increasing the "Base Square Pad" value as shown below. You can also make this smaller as well. Only changing this value should keep the thickness of the lip the same for holding the lens in place.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/EditLensHolder.png" height=425 width=800>

## Drop in Filter Holder

This part is designed to hold a 1 inch filter and can be easily dropped on and off the metal rods if you don't want it to be permanently in place so that nothing else in the system needs to be moved if you want to take it in and out. Again the 1 inch retaining ring can be used to hold the filter in place. Note: You can again increase the "Base Square Pad", however if the filter holder is too thick you won't be able to drop it in between the cage rods. This current thickness works, however I have not yet confirmed the limit on this thickness.

<img src="https://github.com/NanoBioPhotonics-Strathclyde/M4-MultiModal-Modular-Microscopy/blob/main/Images/DropInFilterHolder.png" height=300 width=300>
