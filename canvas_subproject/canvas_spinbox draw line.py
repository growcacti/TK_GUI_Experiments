#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import *

#JH practice 
from tkinter import Tk, Canvas, Frame, BOTH


root = Tk()

root.geometry("1000x1000")
frm=ttk.Frame(root)
frm.grid(row=0, column=0)

from tkinter import *

def display_selected():
    Label(
        text=f'Y', 
        font=('sans-serif', 14),
        bg='#6393A6'
        ).grid(row=1, column=0)


root.title('JH GUI TOOLS')

root.config(bg='#6393A6')

  # default value is 5
x1 = Spinbox(root, from_=1, to=1920, increment=1,
    command=display_selected,
    font=('sans-serif', 18), 

)
x1.grid(row=3, column=0)

y1 = Spinbox(root, from_=1, to=1080, increment=1,
    command=display_selected,
    font=('sans-serif', 18), 

)
y1.grid(row=4, column=0)
x2 = Spinbox(root, from_=1, to=1920, increment=1,
    command=display_selected,
    font=('sans-serif', 18), 

)
x2.grid(row=5, column=0)
y2 = Spinbox(root, from_=1, to=1080, increment=1,
    command=display_selected,
    font=('sans-serif', 18), 

)
y2.grid(row=6, column=0)

#canvas.create_line(x1,y1,x2,y2, fill="green", width=10)

    
def drawline(*args):
     
    canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(), fill="black", width=10)
    print(x1.get(), y1.get(), x2.get(), y2.get())
    

    
root = Tk()  

canvas = Canvas(root, height=800, width=1000)
#canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(),
#    outline="#fb0", fill="#fb0", width=10)
#canvas.create_line(x1, y1, x2, y2,
#    outline="#f50", fill="#f50")
#canvas.create_line(x1, y1, x2, y2,
#    outline="#05f", fill="#05f")
canvas.grid(row=8, column=4)

canvas.bind('<Button-1>', drawline)
click_num=0


btn1 = Button(root, text="set", command=drawline)
btn1.grid(row=8, column=0)

root = Tk()



root.mainloop()
    



