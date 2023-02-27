from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')



def create_grid(window):
    width = 1800
    height = 600
    canvas = Canvas(window, background='white', width=width, height=height)



    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)
    line = canvas.create_line(180,70, 180,100 , fill ='black', width = 7)

    line2 = canvas.create_line(180,100, 180,130 , fill ='black', width = 7)

    line3 = canvas.create_line(180,130, 220,160 , fill ='black', width = 7)

    line4 = canvas.create_line(220,160, 180,190 , fill ='black', width = 7)

    line5 = canvas.create_line(180,190, 220,210, fill ='black', width = 7)

    line6 = canvas.create_line(220,210, 180,240, fill ='black', width = 7)

    line7 = canvas.create_line(180,240, 220,270, fill ='black', width = 7)

    line8 = canvas.create_line(220,270, 180,300 , fill ='black', width = 7)

    line9 = canvas.create_line(180,300, 180,350 , fill ='black', width = 7)

   
    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)

    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)

    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)

    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)


    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)

    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)

    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
    
    
create_grid(window)
window.mainloop()
