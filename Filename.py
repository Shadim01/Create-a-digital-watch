# Digitalwatch
import sys
# importing whole module
from tkinter import *
from tkinter.ttk import *
from time import strftime
import time
# creating tkinter window 
root = Tk()
root.title("A Digital Clock")

def clock():
    Strr = strftime("%a/%H:%M:%S:%p ")
    design.config(text = Strr)
    design.after(100,clock)


# Design the label widget so that clock will look like more attractive 
design = Label(root, font = ('Arial',70, 'bold'),
			background = 'Yellow',
			foreground = 'Black'
                )
design.grid(row = 0,column = 2)
design.pack(anchor = 'center')
clock()
root.mainloop()
