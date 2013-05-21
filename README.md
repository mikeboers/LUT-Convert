LUT Converter
=============

This project contains a Python script which can convert Hald LUTs to the `.cube` format for use in Adobe Photoshop (>= CS 6).

Create a HALD image:

~~~
convert hald:17 identity.png
~~~

Convert it to `cube` format:

~~~
python hald_to_cube.py identity.png identity.cube
~~~

[Read the notes.](NOTES.md)
