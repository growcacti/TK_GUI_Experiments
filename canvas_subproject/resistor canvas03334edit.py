import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import subprocess
import shutil
 

root = tk.Tk()
root.geometry("1920x1080")

canvas = Canvas(root, height=1000, width=1900, bg ="white")
canvas.grid(row=0, column=1)
 



###Resistor Horzontial
##
##line = canvas.create_line(80,70, 120,140 , fill ='black', width = 7)
##
##line2 = canvas.create_line(120,140, 160,70 , fill ='black', width = 7)
##
##line3 = canvas.create_line(161,70, 200,140 , fill ='black', width = 7)
##
##line4 = canvas.create_line(200,140, 240,70 , fill ='black', width = 7)
##
##line5 = canvas.create_line(240,70, 280,140 , fill ='black', width = 7)
##
##line6 = canvas.create_line(280,140, 320,140 , fill ='black', width = 7)
##
##line7 = canvas.create_line(80,70, 40,140 , fill ='black', width = 7)
##
##line8 = canvas.create_line(40,140, 10,140 , fill ='black', width = 7)
##line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)
##
##line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)
##
##line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)
##
##line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)
##
##
##line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)
##
##line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
##line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)
##
##line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
##
##line444 =canvas.create_line(555, 485, 675, 485, 615, 580, 555, 485, fill ='black', width = 7)
##
##line434 =canvas.create_line(550, 580, 680, 580, fill ='black', width = 7)
##
##line4e4 =canvas.create_line(615, 580, 615, 640, fill ='black', width = 7)
##line4e2 =canvas.create_line(615, 485, 615, 440, fill ='black', width = 7)


def checkered(canvas, line_distance):
   #x, y, x2, y2 = 1, 10, 1 , 10
   # vertical lines at an interval of "line_distance" pixel
    for x in range(10, 1000):
       canvas.create_line(x, 0, x, 0, fill = "black", width = 2)
   # horizontal lines at an interval of "line_distance" pixel
    for y in range(10,1000):
        canvas.create_line(0, y, 0, y, fill = "black", width = 2)
checkered(canvas, 10)
##root = tk.Tk()
##e1 = Entry(root)
##e1.grid(row=1, column=1)
##btn1 = Button(root, text="size of gridlines", command=lambda : checkered(canvas, e1.get()))
##btn1.grid(row=3, column=1)
root.mainloop()

#checkered(canvas, 10)

