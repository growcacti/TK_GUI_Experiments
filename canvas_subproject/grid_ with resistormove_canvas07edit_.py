from tkinter import *
from random import *

root = Tk()
root.title('Game Of Life')



def create_grid(root):
    width = 1800
    height = 1000
    canvas = Canvas(root, background='white', width=width, height=height)



    for line in range(0, width, 10): # range(start, stop, step)
        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

    for line in range(0, height, 10):
        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')

    canvas.grid(row=0, column=0)
    line = canvas.create_line(180, 350, 180, 380 , fill ='black', width = 7)

    line2 = canvas.create_line(180, 380, 180, 410, fill ='black', width = 7)

    line3 = canvas.create_line(180,410, 220, 440 , fill ='black', width = 7)

    line4 = canvas.create_line(220,440, 180, 470 , fill ='black', width = 7)

    line5 = canvas.create_line(180, 470, 220, 500, fill ='black', width = 7)

    line6 = canvas.create_line(220, 500, 180, 530, fill ='black', width = 7)

    line7 = canvas.create_line(180, 530, 220, 560, fill ='black', width = 7)

    line8 = canvas.create_line(220, 560, 180, 590 , fill ='black', width = 7)

    line9 = canvas.create_line(180, 590, 180, 640, fill='black', width =7)


root.mainloop()


##
##
##from tkinter import *
##from random import *
##
##root = Tk()
##root.title('Game Of Life')
##
##
##
##def create_grid(root):
##    width = 1800
##    height = 1000
##    canvas = Canvas(root, background='white', width=width, height=height)
##
##
##
##    for line in range(0, width, 10): # range(start, stop, step)
##        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
##
##    for line in range(0, height, 10):
##        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
##
##    canvas.grid(row=0, column=0)
##    line = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line2 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line3 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line4 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line5 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line6 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line7 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line8 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line9 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
####
####   
####    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)
####
####    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)
####
####    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)
####
####    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)
####
####
####    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)
####
####    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
####    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)
####
####    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
####    
####    line444 =canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill ='black', width = 7)
####
####    line434 =canvas.create_line(655, 585, 755, 585, 605, 680, 655, 585, fill ='black', width = 7)
####
####    line4e4 =canvas.create_line(355, 485, 455, 585, 505, 480, 455, 485, fill ='black', width = 7)
####
####
####    line344 =canvas.create_line(755, 785, 655, 785, 605, 680, 755, 785, fill ='black', width = 7)
####    
####
##
##
##
##create_grid(root)
##root.mainloop()
##from tkinter import *
##from random import *
##
##root = Tk()
##root.title('Game Of Life')
##
##
##
##def create_grid(root):
##    width = 1800
##    height = 1000
##    canvas = Canvas(root, background='white', width=width, height=height)
##
##
##
##    for line in range(0, width, 10): # range(start, stop, step)
##        canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')
##
##    for line in range(0, height, 10):
##        canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
##
##    canvas.grid(row=0, column=0)
##    line = canvas.create_line(180, 70, 180, 90 , fill ='black', width = 7)
##
##    line2 = canvas.create_line(180, 90, 180, 120, fill ='black', width = 7)
##
##    line3 = canvas.create_line(180,120, 220, 140 , fill ='black', width = 7)
##
##    line4 = canvas.create_line(220,140, 180,160 , fill ='black', width = 7)
##
##    line5 = canvas.create_line(180,160, 220,180, fill ='black', width = 7)
##
##    line6 = canvas.create_line(220,180, 180,200, fill ='black', width = 7)
##
##    line7 = canvas.create_line(180,200, 220,220, fill ='black', width = 7)
##
##    line8 = canvas.create_line(220,220, 180,240 , fill ='black', width = 7)
##
##    line9 = canvas.create_line(180,240, 180,350 , fill ='black', width = 7)
####
####   
####    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)
####
####    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)
####
####    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)
####
####    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)
####
####
####    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)
####
####    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
####    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)
####
####    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
####    
####    line444 =canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill ='black', width = 7)
####
####    line434 =canvas.create_line(655, 585, 755, 585, 605, 680, 655, 585, fill ='black', width = 7)
####
####    line4e4 =canvas.create_line(355, 485, 455, 585, 505, 480, 455, 485, fill ='black', width = 7)
####
####
####    line344 =canvas.create_line(755, 785, 655, 785, 605, 680, 755, 785, fill ='black', width = 7)
####    
####
##
##
##
##create_grid(root)
##root.mainloop()
## , fill ='black', width = 7)
####
####   
####    line4h = canvas.create_line(680,160, 680,190 , fill ='black', width = 7)
####
####    line5j = canvas.create_line(680,190, 680,210, fill ='black', width = 7)
####
####    line6k = canvas.create_line(680,210, 680,240, fill ='black', width = 7)
####
####    line7l = canvas.create_line(680,240, 680,270, fill ='black', width = 7)
####
####
####    line8 = canvas.create_line(720,270, 640,270 , fill ='black', width = 7)
####
####    line9 = canvas.create_line(680,300, 680,350 , fill ='black', width = 7)
####    line8 = canvas.create_line(640,300, 720,300 , fill ='black', width = 7)
####
####    line93 = canvas.create_line(680,350, 680,470 , fill ='black', width = 7)
####    
####    line444 =canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, fill ='black', width = 7)
####
####    line434 =canvas.create_line(655, 585, 755, 585, 605, 680, 655, 585, fill ='black', width = 7)
####
####    line4e4 =canvas.create_line(355, 485, 455, 585, 505, 480, 455, 485, fill ='black', width = 7)
####
####
####    line344 =canvas.create_line(755, 785, 655, 785, 605, 680, 755, 785, fill ='black', width = 7)
####    
####
##
##
##
##create_grid(root)
##root.mainloop()
