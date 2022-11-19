#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:16:29 2022

@author: svenmaurice
"""


"""
ToDo:
    merged from last to first
    ci interface
    merge-folder argument
"""

from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import os
import re
from PyPDF2 import PdfMerger
##
root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
##
dir_tree = os.walk(folder_selected)
##
msg = messagebox.askquestion(message = "Want to set merge-folder manually?\nOtw. merge-folder will be in selected folder?")
if msg:
    folder_merged = filedialog.askdirectory()
else:
    folder_merged = os.path.join(folder_selected, "merged")
    if not os.path.isdir(folder_merged):
        os.mkdir(folder_merged)
##
def check_pdf(string):
    """
    check if pdf file    
    """
    pattern = pattern = "^.*\.pdf$"
    return(bool(re.match(pattern, string)))
##
for dirpath, dirnames, filenames in dir_tree:
    if dirnames == []:
        ## check if all filenames are of type .pdf
        if not any(list(map(check_pdf, filenames))):
            print("Dir " + dirpath + " contains non pdf type documents!\n")
            continue
        else:
            ## merge
            filenames.sort()
            merge_name = os.path.basename(dirpath)
            merge_pdf = PdfMerger()
            for file_pdf in filenames:
                merge_pdf.append(os.path.join(dirpath, file_pdf))
            ## write
            filename_merged = os.path.join(folder_merged, merge_name)
            merge_pdf.write(filename_merged)
            merge_pdf.close
            print("wrote to " + filename_merged, "\n" )
    else:
        continue