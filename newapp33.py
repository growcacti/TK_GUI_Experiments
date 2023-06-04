import tkinter as tk
from tkinter import ttk
from tkinter import font, IntVar,END
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog

# import tkinter.scrolledtext
from tkinter import font
from tkinter import scrolledtext as st
from tkinter import *
import tkinter.colorchooser
import os, pathlib
import pyautogui as pg
import pyperclip as pc
import glob
import time


class Ooder(object):

    def __init__(self, parent):
        self.parent = parent
        self.top = Toplevel()
        self.font1 = font.Font(family="Chancery Uralic", size=16, weight="bold")
        self.font2 = font.Font(family="Arial", size=16, weight="bold")
        self.frm1 = ttk.Frame(self.parent, width=1200, height=900)
        self.frm1.grid(row=1, column=4)
        self.f1 = ttk.Frame(self.parent,width=100, height=30)
        self.f1.grid(row=10, column=0)
        tk.Label(self.f1, text="From JH APPS", font=self.font1).grid(row=0,column=2)
        tk.Label(self.f1, text="AUTO TILER", font=self.font2).grid(row=1,column=2)
        self.btn1 = tk.Button(self.frm1, text="find x y", bg="orange", bd=6, command=self.print_mouse_position)
        self.btn1.grid(row=5, column=4)
       
       
        tk.Label(self.f1, text="                            x1                                       &" ).grid(row=2, column=2)
        tk.Label(self.f1, text="                     x2").grid(row=2, column=4)

        self.e1 = tk.Entry(self.f1, bd=20, width=20, bg='wheat')
        self.e1.grid(row=5, column=2)
        self.e2 = tk.Entry(self.f1, bd=20, width=20, bg='snow')
        self.e2.grid(row=5, column=4)
        tk.Label(self.f1, text="                            y1                                       &").grid(row=6, column=2)
        tk.Label(self.f1, text="                    y2").grid(row=6, column=4)

        self.e3 = tk.Entry(self.f1, bd=20, width=20, bg='cornsilk') 
        self.e3.grid(row=7, column=2)
        self.e4 = tk.Entry(self.f1, bd=20, width=20, bg='snow')
        self.e4.grid(row=7, column=4)
        self.step = IntVar()
        self.step.set(20)
        tk.Label(self.f1, text="Step Size").grid(row=3, column=6)
        self.sp = Spinbox(self.f1, from_ = 1 , to = 2000, textvariable = self.step)
        self.sp.grid(row=9,column=6)
        self.x1 = self.e1.get()
        self.x2 = self.e2.get()
        self.y1 = self.e3.get()
        self.y2 = self.e4.get()
   
        self.btn6 = tk.Button(self.frm1, text="send hort", bg="orange", bd=6,
                              command=self.newmoveset)
        self.btn6.grid(row=11, column=4)
        self.btn7 = tk.Button(self.frm1, text="send vert", bg="orange", bd=6,
                              command=self.vert)
        self.btn7.grid(row=13, column=4)
        self.btn8 = tk.Button(self.frm1, text="send both x then y", bg="orange", bd=6,
                              command=self.bothmoveset)
        self.btn8.grid(row=14, column=4)
        self.btn9 = tk.Button(self.frm1, text="send both y then x", bg="orange", bd=6,
                              command=self.bothmoveset2)
        self.btn9.grid(row=16, column=4)
    def print_mouse_position(self):
        while True:
            time.sleep(5)
            x, y = pg.position()
            positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(positionStr)

    def new_move(self):
        for i in range(1600, 1700, 20):
            pg.moveTo(i, 550, 2)
            pg.click(i, 550)


    def vert(self):
        x1_entry_value = self.e1.get()
        x2_entry_value = self.e2.get()
        y1_entry_value = self.e3.get()
        y2_entry_value = self.e4.get()
        self.step = int(self.sp.get())
        if y1_entry_value and y2_entry_value and x1_entry_value:
            self.x1 = int(x1_entry_value)
            self.x2 = int(x2_entry_value)
            self.y1 = int(y1_entry_value)
            self.y2 = int(y2_entry_value)

            for j in range(self.y1, self.y2, self.step):
                pg.moveTo(self.x1, j, 1)
                pg.click(self.x1, j)
        else:
            print("Please enter values in all fields.")


    def newmoveset(self):
        x1_entry_value = self.e1.get()
        x2_entry_value = self.e2.get()
        y1_entry_value = self.e3.get()
        y2_entry_value = self.e4.get()
        self.step = int(self.sp.get())
        if x1_entry_value and x2_entry_value and y1_entry_value:
            self.x1 = int(x1_entry_value)
            self.x2 = int(x2_entry_value)
            self.y1 = int(y1_entry_value)
            self.y2 = int(y2_entry_value)

            for i in range(self.x1, self.x2, self.step):
                pg.moveTo(i, self.y1, 1)
                pg.click(i, self.y1)
        else:
            print("Please enter values in all fields.")
    def bothmoveset(self):
        x1_entry_value = self.e1.get()
        x2_entry_value = self.e2.get()
        y1_entry_value = self.e3.get()
        y2_entry_value = self.e4.get()
        self.step = int(self.sp.get())
        if x1_entry_value and x2_entry_value and y1_entry_value:
            self.x1 = int(x1_entry_value)
            self.x2 = int(x2_entry_value)
            self.y1 = int(y1_entry_value)
            self.y2 = int(y2_entry_value)

            for i in range(self.x1, self.x2, self.step):
                for j in range(self.y1, self.y2, self.step):
                
                    pg.moveTo(i, j, 0.5)
                    pg.click(i, j)
        else:
            print("Please enter values in all fields.")

    def bothmoveset2(self):
        x1_entry_value = self.e1.get()
        x2_entry_value = self.e2.get()
        y1_entry_value = self.e3.get()
        y2_entry_value = self.e4.get()
        self.step = int(self.sp.get())
        if x1_entry_value and x2_entry_value and y1_entry_value:
            self.x1 = int(x1_entry_value)
            self.x2 = int(x2_entry_value)
            self.y1 = int(y1_entry_value)
            self.y2 = int(y2_entry_value)

            for j in range(self.y1, self.y2, self.step):
                for i in range(self.x1, self.x2, self.step):
                
                    pg.moveTo(i, j, 0.5)
                    pg.click(i, j)
        else:
            print("Please enter values in all fields.")



class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        c = Ooder(self)
        self.geometry('1200x600')
        self.resizable(True, True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

