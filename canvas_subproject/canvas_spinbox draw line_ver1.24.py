#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser
import os
import sys
import subprocess
import shutil
from PIL import Image, ImageTk
import runpy


#JH practice 
from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH




root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

#root.config(bg='#6393A6')
root.geometry("1000x800")



f0 = ttk.Frame(notebook)
f0.grid(row=0, column=0)



#f5 = ttk.Frame(notebook)

def clr_canvas():
    canvas.delete('all')
    


notebook.add(f0, text="0")

f1 = ttk.Frame(notebook)
notebook.add(f1,text="1")



def drawline(*args):
     
    canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(), fill="black", width=10)
    xx1 = x1.get()
    yy1 = y1.get()
    xx2 = x2.get()
    yy2 = y2.get()

    txt_edit.insert(tk.END, "X1  ")
    txt_edit.insert(tk.END, x1.get())
    txt_edit.insert(tk.END, "   ")
    txt_edit.insert(tk.END, "Y1  ")
    txt_edit.insert(tk.END, y1.get())
    txt_edit.insert(tk.END, "    ")
    txt_edit.insert(tk.END, "X2  ")
    txt_edit.insert(tk.END, x2.get())
    txt_edit.insert(tk.END, "    ")
    txt_edit.insert(tk.END, "Y2  ")
    txt_edit.insert(tk.END, y2.get())
    txt_edit.insert(tk.END, "    ")
    
    rise = float(yy2) - float(yy1)
    run = float(xx2) - float(xx1)
    if run == 0:
        run = rise
        txt_edit.insert(tk.END, "slope=  ")
        txt_edit.insert(tk.END, rise)
    else:
        m = float(rise) / float(run)
        txt_edit.insert(tk.END, "slope=  ")
        txt_edit.insert(tk.END, m)

    txt_edit.insert(tk.END, "  \n")
    return                
    



# Draw an oval inside canvas object
#c= canvas.create_oval(100,10,410,200, outline= "red", fill= "#adf123")


# Get and Print the coordinates of the Oval
#print("Coordinates of the object are:", canvas.coords(c))

tk.Label(f0, text="X1", font=("Times New Roman", 18)).grid(row=0,  column=3)
    

tk.Label(f0, text="Y1", font=("Times New Roman", 18)).grid(row=1,  column=3)
tk.Label(f0, text="X2", font=("Times New Roman", 18)).grid(row=2,  column=3)
tk.Label(f0, text="Y2", font=("Times New Roman", 18)).grid(row=3,  column=3)


canvas = tk.Canvas(f0, bg='white', height=800, width=1000)
#canvas.create_line(x1.get(), y1.get(), x2.get(), y2.get(),
#    outline="#fb0", fill="#fb0", width=10)
#canvas.create_line(x1, y1, x2, y2,
#    outline="#f50", fill="#f50")
#canvas.create_line(x1, y1, x2, y2,
#    outline="#05f", fill="#05f")
x1 = Spinbox(f0, from_=1, to=1920, increment=1,
    command=drawline,
    font=('sans-serif', 18), 

)
x1.grid(row=0, column=1)
y1 = Spinbox(f0, from_=1, to=1080, increment=1,
    command=drawline,
    font=('sans-serif', 18), 

)
y1.grid(row=1, column=1)

x2 = Spinbox(f0, from_=1, to=1920, increment=1,
    command=drawline,
    font=('sans-serif', 18), 

)
x2.grid(row=2, column=1)
y2 = Spinbox(f0, from_=1, to=1080, increment=1,
    command=drawline,
    font=('sans-serif', 18), 

)
y2.grid(row=3, column=1)


  # default value is 5
  

#canvas.create_line(x1,y1,x2,y2, fill="green", width=10)

    






canvas.grid(row=8, column=1)

canvas.bind('<Button-1>', drawline)
click_num=0


btn1 = Button(f0, text="set", command=drawline)
btn1.grid(row=0, column=0)



btn2 = Button(f0, text="clear_can", command=clr_canvas)
btn2.grid(row=1, column=0)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)


def clear():
    txt_edit.delete("1.0", tk.END)


txt_edit = tk.Text(f1, height=500, width=500)
fr_buttons = tk.Frame(f1, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=1, column=0)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_save.grid(row=2, column=0)
btn_clear = tk.Button(fr_buttons, text="Clear", command=clr_canvas)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
#btn_grab = tk.Button(fr_buttons, text="Grab", command=ggtxt)
#btn_grab.grid(row=4, column=0)
# btn_s.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")


f2 = ttk.Frame(notebook)
f2.grid(row=0, column=0)
f3 = ttk.Frame(notebook)
f3.grid(row=0, column=0)
f4 = ttk.Frame(notebook)
f4.grid(row=0, column=0)
notebook.add(f2, text="2")
notebook.add(f3, text="3")
notebook.add(f4, text="4")


#if__name__ == '__main__':
root.mainloop()
    



