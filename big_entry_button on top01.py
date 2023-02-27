import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1394
        height=816
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_444=tk.Entry(root)
        GLineEdit_444["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_444["font"] = ft
        GLineEdit_444["fg"] = "#333333"
        GLineEdit_444["justify"] = "center"
        GLineEdit_444["text"] = "Entry"
        GLineEdit_444.place(x=10,y=40,width=1351,height=776)

        GButton_851=tk.Button(root)
        GButton_851["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_851["font"] = ft
        GButton_851["fg"] = "#000000"
        GButton_851["justify"] = "center"
        GButton_851["text"] = "Button"
        GButton_851.place(x=30,y=10,width=70,height=25)
        GButton_851["command"] = self.GButton_851_command

        GButton_4=tk.Button(root)
        GButton_4["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_4["font"] = ft
        GButton_4["fg"] = "#000000"
        GButton_4["justify"] = "center"
        GButton_4["text"] = "Button"
        GButton_4.place(x=110,y=10,width=70,height=25)
        GButton_4["command"] = self.GButton_4_command

        GButton_235=tk.Button(root)
        GButton_235["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_235["font"] = ft
        GButton_235["fg"] = "#000000"
        GButton_235["justify"] = "center"
        GButton_235["text"] = "Button"
        GButton_235.place(x=190,y=10,width=70,height=25)
        GButton_235["command"] = self.GButton_235_command

        GButton_859=tk.Button(root)
        GButton_859["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_859["font"] = ft
        GButton_859["fg"] = "#000000"
        GButton_859["justify"] = "center"
        GButton_859["text"] = "Button"
        GButton_859.place(x=270,y=10,width=70,height=25)
        GButton_859["command"] = self.GButton_859_command

        GButton_20=tk.Button(root)
        GButton_20["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_20["font"] = ft
        GButton_20["fg"] = "#000000"
        GButton_20["justify"] = "center"
        GButton_20["text"] = "Button"
        GButton_20.place(x=350,y=10,width=70,height=25)
        GButton_20["command"] = self.GButton_20_command

        GButton_308=tk.Button(root)
        GButton_308["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_308["font"] = ft
        GButton_308["fg"] = "#000000"
        GButton_308["justify"] = "center"
        GButton_308["text"] = "Button"
        GButton_308.place(x=430,y=10,width=70,height=25)
        GButton_308["command"] = self.GButton_308_command

        GButton_52=tk.Button(root)
        GButton_52["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_52["font"] = ft
        GButton_52["fg"] = "#000000"
        GButton_52["justify"] = "center"
        GButton_52["text"] = "Button"
        GButton_52.place(x=510,y=10,width=70,height=25)
        GButton_52["command"] = self.GButton_52_command

        GButton_403=tk.Button(root)
        GButton_403["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_403["font"] = ft
        GButton_403["fg"] = "#000000"
        GButton_403["justify"] = "center"
        GButton_403["text"] = "Button"
        GButton_403.place(x=590,y=10,width=70,height=25)
        GButton_403["command"] = self.GButton_403_command

        GButton_890=tk.Button(root)
        GButton_890["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_890["font"] = ft
        GButton_890["fg"] = "#000000"
        GButton_890["justify"] = "center"
        GButton_890["text"] = "Button"
        GButton_890.place(x=670,y=10,width=70,height=25)
        GButton_890["command"] = self.GButton_890_command

        GButton_475=tk.Button(root)
        GButton_475["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_475["font"] = ft
        GButton_475["fg"] = "#000000"
        GButton_475["justify"] = "center"
        GButton_475["text"] = "Button"
        GButton_475.place(x=750,y=10,width=70,height=25)
        GButton_475["command"] = self.GButton_475_command

        GButton_627=tk.Button(root)
        GButton_627["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_627["font"] = ft
        GButton_627["fg"] = "#000000"
        GButton_627["justify"] = "center"
        GButton_627["text"] = "Button"
        GButton_627.place(x=830,y=10,width=70,height=25)
        GButton_627["command"] = self.GButton_627_command

        GButton_228=tk.Button(root)
        GButton_228["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_228["font"] = ft
        GButton_228["fg"] = "#000000"
        GButton_228["justify"] = "center"
        GButton_228["text"] = "Button"
        GButton_228.place(x=910,y=10,width=70,height=25)
        GButton_228["command"] = self.GButton_228_command

        GButton_411=tk.Button(root)
        GButton_411["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_411["font"] = ft
        GButton_411["fg"] = "#000000"
        GButton_411["justify"] = "center"
        GButton_411["text"] = "Button"
        GButton_411.place(x=990,y=10,width=70,height=25)
        GButton_411["command"] = self.GButton_411_command

        GButton_492=tk.Button(root)
        GButton_492["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_492["font"] = ft
        GButton_492["fg"] = "#000000"
        GButton_492["justify"] = "center"
        GButton_492["text"] = "Button"
        GButton_492.place(x=1070,y=10,width=70,height=25)
        GButton_492["command"] = self.GButton_492_command

        GButton_643=tk.Button(root)
        GButton_643["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_643["font"] = ft
        GButton_643["fg"] = "#000000"
        GButton_643["justify"] = "center"
        GButton_643["text"] = "Button"
        GButton_643.place(x=1150,y=10,width=70,height=25)
        GButton_643["command"] = self.GButton_643_command

        GButton_523=tk.Button(root)
        GButton_523["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_523["font"] = ft
        GButton_523["fg"] = "#000000"
        GButton_523["justify"] = "center"
        GButton_523["text"] = "Button"
        GButton_523.place(x=1230,y=10,width=70,height=25)
        GButton_523["command"] = self.GButton_523_command

    def GButton_851_command(self):
        print("command")


    def GButton_4_command(self):
        print("command")


    def GButton_235_command(self):
        print("command")


    def GButton_859_command(self):
        print("command")


    def GButton_20_command(self):
        print("command")


    def GButton_308_command(self):
        print("command")


    def GButton_52_command(self):
        print("command")


    def GButton_403_command(self):
        print("command")


    def GButton_890_command(self):
        print("command")


    def GButton_475_command(self):
        print("command")


    def GButton_627_command(self):
        print("command")


    def GButton_228_command(self):
        print("command")


    def GButton_411_command(self):
        print("command")


    def GButton_492_command(self):
        print("command")


    def GButton_643_command(self):
        print("command")


    def GButton_523_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
