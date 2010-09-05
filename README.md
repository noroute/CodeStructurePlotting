CodeStructurePlotting
=====================

This is very basic Python script that makes it easy to find
code duplication by looking at the "shape" of code from an
eagle-eye perspective.

The script displays all the files passed to it in a single
window in thumbnail size. You should be able to spot code
duplication by scanning similar shapes.

The basic idea is not mine, I got it from a Google Talk or
a book a while ago but I can't exactly remember. If you
happen to now who presented this idea, drop me a note so
I can add attributions.

Use
---
Easy.

 find <DIR> -name <PATTERN> | xargs plotFiles.py

Requirements
------------
The script uses Tk. Now other dependencies are known (besides
Python).

License
-------
The code is covered by GPLv3.

Florian Thiel <code@noroute.de>
