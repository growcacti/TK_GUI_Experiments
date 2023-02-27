import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1361
        height=881
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_789=tk.Entry(root)
        GLineEdit_789["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_789["font"] = ft
        GLineEdit_789["fg"] = "#333333"
        GLineEdit_789["justify"] = "center"
        GLineEdit_789["text"] = "Entry"
        GLineEdit_789.place(x=30,y=80,width=598,height=742)

        GLineEdit_652=tk.Entry(root)
        GLineEdit_652["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_652["font"] = ft
        GLineEdit_652["fg"] = "#333333"
        GLineEdit_652["justify"] = "center"
        GLineEdit_652["text"] = "Entry"
        GLineEdit_652.place(x=680,y=80,width=661,height=737)

        GButton_724=tk.Button(root)
        GButton_724["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_724["font"] = ft
        GButton_724["fg"] = "#000000"
        GButton_724["justify"] = "center"
        GButton_724["text"] = "Button"
        GButton_724.place(x=50,y=30,width=70,height=25)
        GButton_724["command"] = self.GButton_724_command

        GButton_397=tk.Button(root)
        GButton_397["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_397["font"] = ft
        GButton_397["fg"] = "#000000"
        GButton_397["justify"] = "center"
        GButton_397["text"] = "Button"
        GButton_397.place(x=230,y=30,width=70,height=25)
        GButton_397["command"] = self.GButton_397_command

        GButton_244=tk.Button(root)
        GButton_244["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_244["font"] = ft
        GButton_244["fg"] = "#000000"
        GButton_244["justify"] = "center"
        GButton_244["text"] = "Button"
        GButton_244.place(x=320,y=30,width=70,height=25)
        GButton_244["command"] = self.GButton_244_command

        GButton_844=tk.Button(root)
        GButton_844["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_844["font"] = ft
        GButton_844["fg"] = "#000000"
        GButton_844["justify"] = "center"
        GButton_844["text"] = "Button"
        GButton_844.place(x=690,y=30,width=70,height=25)
        GButton_844["command"] = self.GButton_844_command

        GButton_676=tk.Button(root)
        GButton_676["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_676["font"] = ft
        GButton_676["fg"] = "#000000"
        GButton_676["justify"] = "center"
        GButton_676["text"] = "Button"
        GButton_676.place(x=770,y=30,width=70,height=25)
        GButton_676["command"] = self.GButton_676_command

        GButton_211=tk.Button(root)
        GButton_211["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_211["font"] = ft
        GButton_211["fg"] = "#000000"
        GButton_211["justify"] = "center"
        GButton_211["text"] = "Button"
        GButton_211.place(x=940,y=30,width=70,height=25)
        GButton_211["command"] = self.GButton_211_command

        GButton_674=tk.Button(root)
        GButton_674["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_674["font"] = ft
        GButton_674["fg"] = "#000000"
        GButton_674["justify"] = "center"
        GButton_674["text"] = "Button"
        GButton_674.place(x=140,y=30,width=70,height=25)
        GButton_674["command"] = self.GButton_674_command

        GButton_899=tk.Button(root)
        GButton_899["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_899["font"] = ft
        GButton_899["fg"] = "#000000"
        GButton_899["justify"] = "center"
        GButton_899["text"] = "Button"
        GButton_899.place(x=860,y=30,width=70,height=25)
        GButton_899["command"] = self.GButton_899_command

    def GButton_724_command(self):
        print("command")


    def GButton_397_command(self):
        print("command")


    def GButton_244_command(self):
        print("command")


    def GButton_844_command(self):
        print("command")


    def GButton_676_command(self):
        print("command")


    def GButton_211_command(self):
        print("command")


    def GButton_674_command(self):
        print("command")


    def GButton_899_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
