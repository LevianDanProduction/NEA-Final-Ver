from pathlib import Path
import pygame
import os

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import *
"""from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage"""
from tkinter import messagebox
from tkinter import filedialog
import platform
import subprocess
import assembler
AssemblerGui = assembler.Assembler()

import sys
print(sys.path)
CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
sys.path.append(PARENT)
print(sys.path[len(sys.path)-1])

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

import webbrowser

def callback(url):
    webbrowser.open_new(url)

    
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def startTemp():
    print("Start Pseudo Interpreter")
    f = open("settings.txt", "w")
    read = f.write("0")
    f.close()
    subprocess.run("__main__.py", shell=True)

def saveFile():
    try:
        currdir = os.getcwd()
        currdir = currdir + "\\projects"
        tempdir = filedialog.asksaveasfilename(initialdir=currdir, defaultextension='.txt' ,title='Please save the file', filetypes=[("Text Files", "*.txt")])
        print(tempdir)
        f = open(tempdir, "w")
        f.write(editor.get(1.0, END))
        f.close()
        messagebox.showinfo("Done","File Successfully saved")
        print("Done!")
    except:
        print(messagebox.showerror("Error", "Couldn't save file. Please try again."))
        

def openFile():
        try:
            currdir = os.getcwd()
            currdir = currdir + "\\projects"
            tempdir = filedialog.askopenfilename(initialdir=currdir, title='Please select a file', filetypes=[("Text Files", "*.txt")])
            print(tempdir)
            f = open(tempdir, "r")
            content = f.read()
            editor.delete(1.0,END)
            editor.insert(END, content)
            f.close()
            print("Done!")
        except:
            print(messagebox.showerror("Error", "Couldn't load file. Please try again."))

def exportFile():
    currdir = os.getcwd()
    currdir = currdir + "\\projects"
    tempdir = filedialog.asksaveasfilename(initialdir=currdir, defaultextension='.bin' ,title='Please export the file', filetypes=[("bin Files", "*.ch8")])
    print(tempdir)
    f = open(tempdir, "bw")
    f2 = open("assemble.txt", "w")
    f2.write(editor.get(1.0, END))
    f2.close()
    f2 = open("assemble.txt", "r")
    AssemblerGui.splitTextField(f2.read().splitlines())
    print("c")
    f2.close()
    print(AssemblerGui.currentCode)
    AssemblerGui.convertIntoBin()

    savelist = AssemblerGui.binDump()
    print(savelist)
    print("1")
    for item in savelist:
        if item == None:
            continue
        f.write(item)
    f.close()
    messagebox.showinfo("Done","File Successfully exported")
    print("Done!")




def quitWin():
    window.destroy()

window = tk.Tk()

window.geometry("928x778")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 778,
    width = 928,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0) #problem
canvas.create_rectangle(
    0.0,
    0.0,
    928.0,
    778.0,
    fill="#CDCDCD",
    outline="")

canvas.create_rectangle(
    413.0,
    0.0,
    928.0,
    515.0,
    fill="#E9E9E9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    208.0,
    224.0,
    image=entry_image_1
)
editor = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
editor .place(
    x=0.0,
    y=0.0,
    width=416.0,
    height=446.0
)

canvas.create_rectangle(
    1.0,
    512.0,
    928.0,
    778.0,
    fill="#ADA9C4",
    outline="")


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=150.0,
    y=456.0,
    width=114.0,
    height=48.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_2.place(
    x=19.0,
    y=456.0,
    width=114.0,
    height=48.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: startTemp(),
    relief="flat"
)
button_3.place(
    x=282.0,
    y=456.0,
    width=114.0,
    height=48.0
)

def about():
    messagebox.showinfo('DanChip8', 'By Daniel K Version 1.0')
def info():
    messagebox.showinfo('EmulatorControls', 'Buttons: 1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f')
    messagebox.showinfo('DebugEmuatorControls', 'Show Current Data : M ')
def linktodoc():
    callback("http://devernay.free.fr/hacks/chip8/C8TECH10.HTM")
def newprompt():
    messageBox = messagebox.askyesno("NEW?", "Do you want to start a new project?")
    if messageBox == True:
        editor.delete(1.0,END)
    else:
        print("ok")


    
menubar = Menu(window, background='white', foreground='black', activebackground='white', activeforeground='black')  
file = Menu(menubar, tearoff=1, background='white', foreground='black')  
file.add_command(label="New",command=lambda:newprompt())  
file.add_command(label="Open",command=lambda:openFile())    
file.add_command(label="Save as",command=lambda:saveFile())    
file.add_command(label="Export",command=lambda:exportFile())  
file.add_separator()  
file.add_command(label="Exit", command=lambda:quitWin())  
menubar.add_cascade(label="File", menu=file)  

edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()     
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
menubar.add_cascade(label="Edit", menu=edit)  
help = Menu(menubar, tearoff=0)  
help.add_command(label="About", command=lambda:about())
help.add_command(label="Controls", command=lambda:info())
menubar.add_cascade(label="Help", menu=help)
help.add_cascade(label="Doc's" ,command=lambda:linktodoc())


window.config(menu=menubar)
window.mainloop()

f = open("settings.txt", "w")
f.write("1")
f.close()

#window.resizable(False, False)

"""embed = tk.Frame(window)

canvas.create_window(416,128, anchor = "nw", window = embed, width = 512, height = 256)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
cWindow = Display()
screen = cWindow.gameDisplay"""

'''
pygame.display.init()


while True():
    pygame.display.update()
    window.update()
'''

