from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')



def create_grid(window):
    width = 800
    height = 600
    canvas = Canvas(window, background='white', width=width, height=height)



    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)
    line = canvas.create_line(80,70, 120,140 , fill ='black', width = 7)

    line2 = canvas.create_line(120,140, 160,70 , fill ='black', width = 7)

    line3 = canvas.create_line(161,70, 200,140 , fill ='black', width = 7)

    line4 = canvas.create_line(200,140, 240,70 , fill ='black', width = 7)

    line5 = canvas.create_line(240,70, 280,140 , fill ='black', width = 7)

    line6 = canvas.create_line(280,140, 320,140 , fill ='black', width = 7)

    line7 = canvas.create_line(80,70, 40,140 , fill ='black', width = 7)

    line8 = canvas.create_line(40,140, 10,140 , fill ='black', width = 7)


create_grid(window)
window.mainloop()
