# IonioNET
A ''Deep Learning and Remote Sensing Applications'' project aiming to detect Agricultural and Non-Agricultural land cover.
 The IonioNET dataset provided is Sentinel-2A images of  Kerkira, Paxoi, Kefalonia, Lefkada, Meganisi, Ithaka,
 Corfu and Kithira islands of Ionion sea, Greece.

The archive was constructed by selecting Sentinel-2A
tiles acquired between January 2017 and April 2019.
The dataset contains raw satellite images and their corresponding ground truth according to Corine Land Cover 2018 . 
Noticeable differences were present in the fields at summer
months, mostly dry soil, in comparison with the winter ones.
Since optical satellite imagery may be contaminated with
clouds and shadows, preliminary processing steps were
taken to clean the data. Otherwise, contaminated data would
distract the training procedure with irrelevant pixel values.

The initial tiles were exported in a map scale of 1/30.000
through Qgis software using Sentinel’s Hub plugin in the following
forms a) Georeferenced TIFF images (Reference System
WGS 84 Pseudo Merctor) and b) JPG images.

Here is the area of Interest in Greece where the tiles were extracted from:


An example of raw image tile:
![4 april_kef6_](https://user-images.githubusercontent.com/27006471/58387888-69454680-801f-11e9-83f8-732ac3daaefd.jpg)



An example of the corresponding ground truth of the tile above according to CLC 2018:


Finally, here lies the official legend of Corine Land Cover with its 44 classes.
Our project is targeting to detect only categories from 2nd level of the legend i.e Agricultural Areas.
The rest of the categories were labelled as non Agricultural.
