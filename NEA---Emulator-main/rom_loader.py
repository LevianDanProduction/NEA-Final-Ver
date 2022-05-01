"This module defines a Rom Loader function for loading roms"
from tkinter import filedialog as fd
from tkinter import messagebox
import os


"""This method loads the bytes from a rom using file explorer"""

def LoadBrowse():
    try:
        currDir = os.getcwd()
        currDir = currDir + "\\roms"
        tempDir = fd.askopenfilename(initialdir=currDir, title='Please select a file', filetypes=[(".ch8 Files", "*.ch8")])
        print(tempDir)
        with open(tempDir, "rb") as file:
            fileBytes = file.read()
            print(fileBytes)
            print("Load Success")
            return fileBytes
    except:
        print(messagebox.showerror("Error", "Couldn't load file. Please try again."))



"""This method loads the bytes from a rom from the temp rom folder"""


def LoadTemp(romName):
    try:
        with open("temp.ch8", "rb") as file:
            fileBytes = file.read()
            print("Load Success")
            return fileBytes
    except:
        print(messagebox.showerror("Error", "Couldn't load file. Please try again."))
        
