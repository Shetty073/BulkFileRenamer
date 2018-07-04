#!/usr/bin/python3
'''

Bulk File Renamer
Author: AlphaSierra aka Ashish Shetty
Python Version: 3.6

Run this script in the same folder in which the files to rename are kept then
execute. It will ask for the new file name enter it and your files will be renamed.
Each file will have same name (which you previously entered) alongside a unique no.
starting with 0.
For e.g.
ls
> abc.jpg foo.jpg bar.jpg

Consider a folder containing the above files

Now after running the script to rename these lets say we entered "alpha" as our new name.
Now the above files will be renamed as:
alpha0.jpg alpha1.jpg alpha2.jpg

'''

import os

path = os.getcwd()
filenames = os.listdir(path)
i = 0
namefile = input("Enter the new filename you want: ")

for filename in filenames:
	if filename == os.path.basename(__file__):
		pass
	else:
		filenm, fileext = os.path.splitext(filename)
		os.rename(os.path.join(path, filename), os.path.join(path, namefile + str(i) + fileext))
		i = i + 1
