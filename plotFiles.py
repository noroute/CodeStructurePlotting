#!/usr/bin/env python

# Copyright 2010 by Florian Thiel <code@noroute.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import glob
import math
from Tkinter import *

filename_font = ("courier" "6")
contents_font = ("courier", "3")

class TextStructureView(Frame):
    """Display any number of text files in a really small font together
    in a Frame. This is useful to spot code duplication by looking at
    the 'shape' of the code. This is an idea from Martin Fowler or anyone
    from the Refactoring crowd, unfortunately I can't remember where I first
    heard of this method.
    """
    def __init__(self, master, files):
        """Draw a frame with thumbnails of all files passed ordered in a grid.
        Be warned, if you pass large numbers of files you will get huge windows.
        """
        Frame.__init__(self, master, height=800, width=800)
        nr_files = len(files)
        if(nr_files == 0):
            return
        rows = int(math.sqrt(nr_files))
        cols = int(nr_files / rows)
        self.pack(fill=BOTH, expand=1)
        for i in range(len(files)):
            f = self.drawOneFile(files[i])
            this_col = int(i % cols)
            this_row = int(i / cols)
            f.grid(row = this_row, column = this_col)
            
    def drawOneFile(self, name_contents_tuple):
        f = Frame(self)
        filename = Label(f, text=os.path.basename(name_contents_tuple[0]),
                         font=filename_font)
        filename.pack()
        contents = Text(f, font=contents_font)
        contents.insert(END, name_contents_tuple[1])
        contents.config(state=DISABLED, width=90, height=100)
        contents.pack(fill=BOTH)
        return f

def generateNameContentsTuples(filenames):
    filelist = []
    for name in filenames:
        filelist.append( (name, open(name, 'r').read()) )
    return filelist

def main(arguments):
    filenames = arguments
    root = Tk()
    files = generateNameContentsTuples(filenames)
    view = TextStructureView(root,files)
    root.mainloop()

if __name__ == '__main__':
    # exclude name of this file
    main(sys.argv[1:])
