# -*- coding: utf-8 -*-
"""
@author Sven Maurice Morlock
@date 2021-11-25

write file names in specified folder in a .txt file
"""

from tkinter import filedialog
from tkinter import *
from os import listdir
from os.path import isfile, join
from math import floor

root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
len_line = 78
linesymbol = "#"
filename = "file_summary"
files = [file for file in listdir(folder_selected) if isfile(join(folder_selected, file))]
lines_to_write = []


# adjust filename to row format used in txt file
for file in files:
    len_file = len(file)
    if len_file < 78:
        residual = (78 - len_file) - 1 # one sign is added always
        line_to_write  = (1 + floor(residual / 2)) * linesymbol + str(file) + (residual - floor(residual / 2)) * linesymbol
    else:
        line_to_write = linesymbol + str(file)
    lines_to_write.append(line_to_write)
    
print(len(lines_to_write))
lines_to_write = [line + "\n" for line in lines_to_write]
print(lines_to_write)
# write filename
with  open(filename, "a") as textfile:
    textfile.writelines(lines_to_write)
    print("written!")