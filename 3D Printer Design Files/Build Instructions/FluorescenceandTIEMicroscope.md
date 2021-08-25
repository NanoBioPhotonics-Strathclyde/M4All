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

STL files to print:

* 1x 1 Inch Dichroic Holder
* 4x 1 Inch Lens Holder
* 4x 1 Inch Retaining Ring
* 1x 45 Degree Mirror Holder
* 1x Dichroic Locker
* 4x Drop In Filter Holder
* 1 x Fluorescence Branch
* 3x TIE Branch
* 3x Raspberry Pi Camera V2 Holder

