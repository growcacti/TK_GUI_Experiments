import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1331
        height=792
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_308=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_308["font"] = ft
        GLabel_308["fg"] = "#333333"
        GLabel_308["justify"] = "center"
        GLabel_308["text"] = "label"
        GLabel_308.place(x=210,y=50,width=70,height=25)

        GLineEdit_12=tk.Entry(root)
        GLineEdit_12["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_12["font"] = ft
        GLineEdit_12["fg"] = "#333333"
        GLineEdit_12["justify"] = "center"
        GLineEdit_12["text"] = "Entry"
        GLineEdit_12.place(x=0,y=180,width=490,height=329)

        GLabel_310=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_310["font"] = ft
        GLabel_310["fg"] = "#333333"
        GLabel_310["justify"] = "center"
        GLabel_310["text"] = "label"
        GLabel_310.place(x=1040,y=50,width=70,height=25)

        GLineEdit_941=tk.Entry(root)
        GLineEdit_941["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_941["font"] = ft
        GLineEdit_941["fg"] = "#333333"
        GLineEdit_941["justify"] = "center"
        GLineEdit_941["text"] = "Entry"
        GLineEdit_941.place(x=830,y=160,width=458,height=354)

        GButton_52=tk.Button(root)
        GButton_52["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_52["font"] = ft
        GButton_52["fg"] = "#000000"
        GButton_52["justify"] = "center"
        GButton_52["text"] = "Button"
        GButton_52.place(x=60,y=570,width=70,height=25)
        GButton_52["command"] = self.GButton_52_command

        GButton_669=tk.Button(root)
        GButton_669["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_669["font"] = ft
        GButton_669["fg"] = "#000000"
        GButton_669["justify"] = "center"
        GButton_669["text"] = "Button"
        GButton_669.place(x=150,y=570,width=70,height=25)
        GButton_669["command"] = self.GButton_669_command

        GButton_644=tk.Button(root)
        GButton_644["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_644["font"] = ft
        GButton_644["fg"] = "#000000"
        GButton_644["justify"] = "center"
        GButton_644["text"] = "Button"
        GButton_644.place(x=240,y=570,width=70,height=25)
        GButton_644["command"] = self.GButton_644_command

        GButton_278=tk.Button(root)
        GButton_278["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_278["font"] = ft
        GButton_278["fg"] = "#000000"
        GButton_278["justify"] = "center"
        GButton_278["text"] = "Button"
        GButton_278.place(x=330,y=570,width=70,height=25)
        GButton_278["command"] = self.GButton_278_command

        GButton_221=tk.Button(root)
        GButton_221["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_221["font"] = ft
        GButton_221["fg"] = "#000000"
        GButton_221["justify"] = "center"
        GButton_221["text"] = "Button"
        GButton_221.place(x=890,y=570,width=70,height=25)
        GButton_221["command"] = self.GButton_221_command

        GButton_859=tk.Button(root)
        GButton_859["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_859["font"] = ft
        GButton_859["fg"] = "#000000"
        GButton_859["justify"] = "center"
        GButton_859["text"] = "Button"
        GButton_859.place(x=980,y=570,width=70,height=25)
        GButton_859["command"] = self.GButton_859_command

        GButton_397=tk.Button(root)
        GButton_397["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_397["font"] = ft
        GButton_397["fg"] = "#000000"
        GButton_397["justify"] = "center"
        GButton_397["text"] = "Button"
        GButton_397.place(x=1070,y=570,width=70,height=25)
        GButton_397["command"] = self.GButton_397_command

        GButton_340=tk.Button(root)
        GButton_340["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_340["font"] = ft
        GButton_340["fg"] = "#000000"
        GButton_340["justify"] = "center"
        GButton_340["text"] = "Button"
        GButton_340.place(x=1160,y=570,width=70,height=25)
        GButton_340["command"] = self.GButton_340_command

    def GButton_52_command(self):
        print("command")


    def GButton_669_command(self):
        print("command")


    def GButton_644_command(self):
        print("command")


    def GButton_278_command(self):
        print("command")


    def GButton_221_command(self):
        print("command")


    def GButton_859_command(self):
        print("command")


    def GButton_397_command(self):
        print("command")


    def GButton_340_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
