import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=135
        height=480
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_130=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_130["font"] = ft
        GLabel_130["fg"] = "#333333"
        GLabel_130["justify"] = "center"
        GLabel_130["text"] = "label"
        GLabel_130.place(x=0,y=40,width=70,height=25)

        GRadio_922=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_922["font"] = ft
        GRadio_922["fg"] = "#333333"
        GRadio_922["justify"] = "center"
        GRadio_922["text"] = "RadioButton"
        GRadio_922.place(x=20,y=60,width=85,height=25)
        GRadio_922["command"] = self.GRadio_922_command

        GLabel_220=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_220["font"] = ft
        GLabel_220["fg"] = "#333333"
        GLabel_220["justify"] = "center"
        GLabel_220["text"] = "label"
        GLabel_220.place(x=0,y=100,width=70,height=25)

        GRadio_906=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_906["font"] = ft
        GRadio_906["fg"] = "#333333"
        GRadio_906["justify"] = "center"
        GRadio_906["text"] = "RadioButton"
        GRadio_906.place(x=20,y=120,width=85,height=25)
        GRadio_906["command"] = self.GRadio_906_command

        GLabel_810=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_810["font"] = ft
        GLabel_810["fg"] = "#333333"
        GLabel_810["justify"] = "center"
        GLabel_810["text"] = "label"
        GLabel_810.place(x=0,y=160,width=70,height=25)

        GRadio_858=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_858["font"] = ft
        GRadio_858["fg"] = "#333333"
        GRadio_858["justify"] = "center"
        GRadio_858["text"] = "RadioButton"
        GRadio_858.place(x=20,y=180,width=85,height=25)
        GRadio_858["command"] = self.GRadio_858_command

        GLabel_899=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_899["font"] = ft
        GLabel_899["fg"] = "#333333"
        GLabel_899["justify"] = "center"
        GLabel_899["text"] = "label"
        GLabel_899.place(x=0,y=230,width=70,height=25)

        GRadio_530=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_530["font"] = ft
        GRadio_530["fg"] = "#333333"
        GRadio_530["justify"] = "center"
        GRadio_530["text"] = "RadioButton"
        GRadio_530.place(x=20,y=250,width=85,height=25)
        GRadio_530["command"] = self.GRadio_530_command

        GLabel_274=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_274["font"] = ft
        GLabel_274["fg"] = "#333333"
        GLabel_274["justify"] = "center"
        GLabel_274["text"] = "label"
        GLabel_274.place(x=0,y=300,width=70,height=25)

        GRadio_818=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_818["font"] = ft
        GRadio_818["fg"] = "#333333"
        GRadio_818["justify"] = "center"
        GRadio_818["text"] = "RadioButton"
        GRadio_818.place(x=20,y=320,width=85,height=25)
        GRadio_818["command"] = self.GRadio_818_command

        GLabel_858=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_858["font"] = ft
        GLabel_858["fg"] = "#333333"
        GLabel_858["justify"] = "center"
        GLabel_858["text"] = "label"
        GLabel_858.place(x=0,y=370,width=70,height=25)

        GRadio_4=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_4["font"] = ft
        GRadio_4["fg"] = "#333333"
        GRadio_4["justify"] = "center"
        GRadio_4["text"] = "RadioButton"
        GRadio_4.place(x=20,y=390,width=85,height=25)
        GRadio_4["command"] = self.GRadio_4_command

        GButton_34=tk.Button(root)
        GButton_34["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_34["font"] = ft
        GButton_34["fg"] = "#000000"
        GButton_34["justify"] = "center"
        GButton_34["text"] = "Button"
        GButton_34.place(x=20,y=430,width=70,height=25)
        GButton_34["command"] = self.GButton_34_command

    def GRadio_922_command(self):
        print("command")


    def GRadio_906_command(self):
        print("command")


    def GRadio_858_command(self):
        print("command")


    def GRadio_530_command(self):
        print("command")


    def GRadio_818_command(self):
        print("command")


    def GRadio_4_command(self):
        print("command")


    def GButton_34_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
