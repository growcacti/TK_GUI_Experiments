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
    line = canvas.create_line(80,70, 220,100 , fill ='black', width = 7)

    line2 = canvas.create_line(220,100, 80,130 , fill ='black', width = 7)

    line3 = canvas.create_line(80,130, 220,160 , fill ='black', width = 7)

    line4 = canvas.create_line(220,160, 80,190 , fill ='black', width = 7)

    line5 = canvas.create_line(80,190, 220,210, fill ='black', width = 7)

    line6 = canvas.create_line(220,210, 80,240, fill ='black', width = 7)

    line7 = canvas.create_line(80,240, 220,270, fill ='black', width = 7)

    line8 = canvas.create_line(220,270, 80,300 , fill ='black', width = 7)


create_grid(window)
window.mainloop()
