import tkinter as tk
from tkinter import Canvas
root = tk.Tk()
root.title("Canvas widgets")
root.geometry("1800x1000")



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


canvas_width = 1800
canvas_height = 900 
w = Canvas(root, 
           width=canvas_width,
           height=canvas_height)
w.grid(row=0, column=0)

checkered(w,20)







 
