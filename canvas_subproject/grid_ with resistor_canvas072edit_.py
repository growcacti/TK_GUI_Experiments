from tkinter import *
from random import *

window = Tk()
window.title('Game Of Life')



def create_grid(window):
    width = 1800
    height = 1000
    canvas = Canvas(window, background='white', width=width, height=height)



    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)
####    line = canvas.create_line(196, 312, 175, 362, fill ='black', width = 7)
####
####    line2 = canvas.create_line(215, 362, 194, 402, fill ='black', width = 7)
####
####    line3 = canvas.create_line(175, 366, 194, 402 , fill ='black', width = 7)
####
####    line4 = canvas.create_line(194, 402, 207, 402 , fill ='black', width = 7)
####
####    line5 = canvas.create_line(175, 402, 246, 462, fill ='black', width = 7)
####
####    line6 = canvas.create_line(435,544, 446, 598, fill ='black', width = 7)
####
##    line7 = canvas.create_line(446, 598, 470, 537, fill ='black', width = 7)
##
##    line8 = canvas.create_line(470, 592, 378, 576 , fill ='black', width = 7)
##
##    line9 = canvas.create_line(530,561, 530, 350 , fill ='black', width = 7)

##   
##    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)
##
##    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)
##
##    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)
##
##    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)
##
##
##    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)
##
##    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
##    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)
##
##    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
    
    line444 =canvas.create_line(855, 485, 975, 485, 915, 580, 855, 485, fill ='black', width = 7)

    line434 =canvas.create_line(850, 580, 980, 580, fill ='black', width = 7)
    line4e4 =canvas.create_line(915, 580, 915, 640, fill ='black', width = 7)
    line4e2 =canvas.create_line(915, 485, 915, 440, fill ='black', width = 7)

##    line344 =canvas.create_line(755, 785, 655, 785, 605, 680, 755, 785, fill ='black', width = 7)
##    
##



create_grid(window)
window.mainloop()
