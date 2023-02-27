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


frm = Frame(root, height=1000, width=1900)
frm.grid(row=0, rowspan=5, column=0, columnspan=5)
canvas = Canvas(frm, height=1000, width=900)

canvas.grid(row=0, rowspan=10, column=0, columnspan=10)




 



###Resistor Horzontial

line = canvas.create_line(80,70, 120,140 , fill ='black', width = 7)

line2 = canvas.create_line(120,140, 160,70 , fill ='black', width = 7)

line3 = canvas.create_line(161,70, 200,140 , fill ='black', width = 7)

line4 = canvas.create_line(200,140, 240,70 , fill ='black', width = 7)

line5 = canvas.create_line(240,70, 280,140 , fill ='black', width = 7)

line6 = canvas.create_line(280,140, 320,140 , fill ='black', width = 7)

line7 = canvas.create_line(80,70, 40,140 , fill ='black', width = 7)

line8 = canvas.create_line(40,140, 10,140 , fill ='black', width = 7)
line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)

line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)

line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)

line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)


line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)

line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)

line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)

line444 =canvas.create_line(555, 485, 675, 485, 615, 580, 555, 485, fill ='black', width = 7)

line434 =canvas.create_line(550, 580, 680, 580, fill ='black', width = 7)

line4e4 =canvas.create_line(615, 580, 615, 640, fill ='black', width = 7)
line4e2 =canvas.create_line(615, 485, 615, 440, fill ='black', width = 7)


def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(10, 1000):
      canvas.create_line(x, y, x2, y2, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(10,1000):
      canvas.create_line(x, y, x2, y2, fill="#476042")




checkered(canvas, 10)

