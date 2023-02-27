import tkinter as tk


from random import *
canvas= tk.Canvas (bg="white" , height = "1000", width ="1000")
canvas.pack()


x=randint(100,900)
y=randint(100,900)
speed=randint(30,80)


canvas.create_oval(x-100, y-100, x+100,y+100, fill="firebrick3", width="2")
canvas.create_oval(x-75, y-75, x+75,y+75, fill="white", width="2")
canvas.create_text(x,y, text=str(speed), font="Calibri 20 bold")
