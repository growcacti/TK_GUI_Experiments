import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1306
        height=94
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_592=tk.Button(root)
        GButton_592["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_592["font"] = ft
        GButton_592["fg"] = "#000000"
        GButton_592["justify"] = "center"
        GButton_592["text"] = "Button"
        GButton_592.place(x=20,y=20,width=70,height=25)
        GButton_592["command"] = self.GButton_592_command

        GButton_89=tk.Button(root)
        GButton_89["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_89["font"] = ft
        GButton_89["fg"] = "#000000"
        GButton_89["justify"] = "center"
        GButton_89["text"] = "Button"
        GButton_89.place(x=100,y=20,width=70,height=25)
        GButton_89["command"] = self.GButton_89_command

        GButton_721=tk.Button(root)
        GButton_721["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_721["font"] = ft
        GButton_721["fg"] = "#000000"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "Button"
        GButton_721.place(x=180,y=20,width=70,height=25)
        GButton_721["command"] = self.GButton_721_command

        GButton_425=tk.Button(root)
        GButton_425["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_425["font"] = ft
        GButton_425["fg"] = "#000000"
        GButton_425["justify"] = "center"
        GButton_425["text"] = "Button"
        GButton_425.place(x=260,y=20,width=70,height=25)
        GButton_425["command"] = self.GButton_425_command

        GButton_818=tk.Button(root)
        GButton_818["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_818["font"] = ft
        GButton_818["fg"] = "#000000"
        GButton_818["justify"] = "center"
        GButton_818["text"] = "Button"
        GButton_818.place(x=980,y=50,width=70,height=25)
        GButton_818["command"] = self.GButton_818_command

        GButton_946=tk.Button(root)
        GButton_946["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_946["font"] = ft
        GButton_946["fg"] = "#000000"
        GButton_946["justify"] = "center"
        GButton_946["text"] = "Button"
        GButton_946.place(x=420,y=20,width=70,height=25)
        GButton_946["command"] = self.GButton_946_command

        GButton_738=tk.Button(root)
        GButton_738["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_738["font"] = ft
        GButton_738["fg"] = "#000000"
        GButton_738["justify"] = "center"
        GButton_738["text"] = "Button"
        GButton_738.place(x=500,y=20,width=70,height=25)
        GButton_738["command"] = self.GButton_738_command

        GButton_612=tk.Button(root)
        GButton_612["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_612["font"] = ft
        GButton_612["fg"] = "#000000"
        GButton_612["justify"] = "center"
        GButton_612["text"] = "Button"
        GButton_612.place(x=580,y=20,width=70,height=25)
        GButton_612["command"] = self.GButton_612_command

        GButton_43=tk.Button(root)
        GButton_43["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_43["font"] = ft
        GButton_43["fg"] = "#000000"
        GButton_43["justify"] = "center"
        GButton_43["text"] = "Button"
        GButton_43.place(x=660,y=20,width=70,height=25)
        GButton_43["command"] = self.GButton_43_command

        GButton_395=tk.Button(root)
        GButton_395["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_395["font"] = ft
        GButton_395["fg"] = "#000000"
        GButton_395["justify"] = "center"
        GButton_395["text"] = "Button"
        GButton_395.place(x=660,y=50,width=70,height=25)
        GButton_395["command"] = self.GButton_395_command

        GButton_92=tk.Button(root)
        GButton_92["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_92["font"] = ft
        GButton_92["fg"] = "#000000"
        GButton_92["justify"] = "center"
        GButton_92["text"] = "Button"
        GButton_92.place(x=740,y=20,width=70,height=25)
        GButton_92["command"] = self.GButton_92_command

        GButton_459=tk.Button(root)
        GButton_459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#000000"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "Button"
        GButton_459.place(x=100,y=50,width=70,height=25)
        GButton_459["command"] = self.GButton_459_command

        GButton_163=tk.Button(root)
        GButton_163["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_163["font"] = ft
        GButton_163["fg"] = "#000000"
        GButton_163["justify"] = "center"
        GButton_163["text"] = "Button"
        GButton_163.place(x=180,y=50,width=70,height=25)
        GButton_163["command"] = self.GButton_163_command

        GButton_91=tk.Button(root)
        GButton_91["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_91["font"] = ft
        GButton_91["fg"] = "#000000"
        GButton_91["justify"] = "center"
        GButton_91["text"] = "Button"
        GButton_91.place(x=260,y=50,width=70,height=25)
        GButton_91["command"] = self.GButton_91_command

        GButton_452=tk.Button(root)
        GButton_452["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_452["font"] = ft
        GButton_452["fg"] = "#000000"
        GButton_452["justify"] = "center"
        GButton_452["text"] = "Button"
        GButton_452.place(x=20,y=50,width=70,height=25)
        GButton_452["command"] = self.GButton_452_command

        GButton_940=tk.Button(root)
        GButton_940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#000000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Button"
        GButton_940.place(x=340,y=50,width=70,height=25)
        GButton_940["command"] = self.GButton_940_command

        GButton_611=tk.Button(root)
        GButton_611["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_611["font"] = ft
        GButton_611["fg"] = "#000000"
        GButton_611["justify"] = "center"
        GButton_611["text"] = "Button"
        GButton_611.place(x=420,y=50,width=70,height=25)
        GButton_611["command"] = self.GButton_611_command

        GButton_491=tk.Button(root)
        GButton_491["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_491["font"] = ft
        GButton_491["fg"] = "#000000"
        GButton_491["justify"] = "center"
        GButton_491["text"] = "Button"
        GButton_491.place(x=500,y=50,width=70,height=25)
        GButton_491["command"] = self.GButton_491_command

        GButton_909=tk.Button(root)
        GButton_909["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_909["font"] = ft
        GButton_909["fg"] = "#000000"
        GButton_909["justify"] = "center"
        GButton_909["text"] = "Button"
        GButton_909.place(x=580,y=50,width=70,height=25)
        GButton_909["command"] = self.GButton_909_command

        GButton_395=tk.Button(root)
        GButton_395["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_395["font"] = ft
        GButton_395["fg"] = "#000000"
        GButton_395["justify"] = "center"
        GButton_395["text"] = "Button"
        GButton_395.place(x=660,y=50,width=70,height=25)
        GButton_395["command"] = self.GButton_395_command

        GButton_819=tk.Button(root)
        GButton_819["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_819["font"] = ft
        GButton_819["fg"] = "#000000"
        GButton_819["justify"] = "center"
        GButton_819["text"] = "Button"
        GButton_819.place(x=740,y=50,width=70,height=25)
        GButton_819["command"] = self.GButton_819_command

        GButton_572=tk.Button(root)
        GButton_572["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_572["font"] = ft
        GButton_572["fg"] = "#000000"
        GButton_572["justify"] = "center"
        GButton_572["text"] = "Button"
        GButton_572.place(x=820,y=20,width=70,height=25)
        GButton_572["command"] = self.GButton_572_command

        GButton_755=tk.Button(root)
        GButton_755["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_755["font"] = ft
        GButton_755["fg"] = "#000000"
        GButton_755["justify"] = "center"
        GButton_755["text"] = "Button"
        GButton_755.place(x=1060,y=50,width=70,height=25)
        GButton_755["command"] = self.GButton_755_command

        GButton_867=tk.Button(root)
        GButton_867["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_867["font"] = ft
        GButton_867["fg"] = "#000000"
        GButton_867["justify"] = "center"
        GButton_867["text"] = "Button"
        GButton_867.place(x=900,y=20,width=70,height=25)
        GButton_867["command"] = self.GButton_867_command

        GButton_606=tk.Button(root)
        GButton_606["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_606["font"] = ft
        GButton_606["fg"] = "#000000"
        GButton_606["justify"] = "center"
        GButton_606["text"] = "Button"
        GButton_606.place(x=900,y=50,width=70,height=25)
        GButton_606["command"] = self.GButton_606_command

        GButton_51=tk.Button(root)
        GButton_51["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_51["font"] = ft
        GButton_51["fg"] = "#000000"
        GButton_51["justify"] = "center"
        GButton_51["text"] = "Button"
        GButton_51.place(x=980,y=20,width=70,height=25)
        GButton_51["command"] = self.GButton_51_command

        GButton_818=tk.Button(root)
        GButton_818["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_818["font"] = ft
        GButton_818["fg"] = "#000000"
        GButton_818["justify"] = "center"
        GButton_818["text"] = "Button"
        GButton_818.place(x=980,y=50,width=70,height=25)
        GButton_818["command"] = self.GButton_818_command

        GButton_26=tk.Button(root)
        GButton_26["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_26["font"] = ft
        GButton_26["fg"] = "#000000"
        GButton_26["justify"] = "center"
        GButton_26["text"] = "Button"
        GButton_26.place(x=1060,y=20,width=70,height=25)
        GButton_26["command"] = self.GButton_26_command

        GButton_755=tk.Button(root)
        GButton_755["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_755["font"] = ft
        GButton_755["fg"] = "#000000"
        GButton_755["justify"] = "center"
        GButton_755["text"] = "Button"
        GButton_755.place(x=1060,y=50,width=70,height=25)
        GButton_755["command"] = self.GButton_755_command

        GButton_788=tk.Button(root)
        GButton_788["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_788["font"] = ft
        GButton_788["fg"] = "#000000"
        GButton_788["justify"] = "center"
        GButton_788["text"] = "Button"
        GButton_788.place(x=1140,y=20,width=70,height=25)
        GButton_788["command"] = self.GButton_788_command

        GButton_83=tk.Button(root)
        GButton_83["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_83["font"] = ft
        GButton_83["fg"] = "#000000"
        GButton_83["justify"] = "center"
        GButton_83["text"] = "Button"
        GButton_83.place(x=1220,y=20,width=70,height=25)
        GButton_83["command"] = self.GButton_83_command

        GButton_978=tk.Button(root)
        GButton_978["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_978["font"] = ft
        GButton_978["fg"] = "#000000"
        GButton_978["justify"] = "center"
        GButton_978["text"] = "Button"
        GButton_978.place(x=1220,y=50,width=70,height=25)
        GButton_978["command"] = self.GButton_978_command

    def GButton_592_command(self):
        print("command")


    def GButton_89_command(self):
        print("command")


    def GButton_721_command(self):
        print("command")


    def GButton_425_command(self):
        print("command")


    def GButton_818_command(self):
        print("command")


    def GButton_946_command(self):
        print("command")


    def GButton_738_command(self):
        print("command")


    def GButton_612_command(self):
        print("command")


    def GButton_43_command(self):
        print("command")


    def GButton_395_command(self):
        print("command")


    def GButton_92_command(self):
        print("command")


    def GButton_459_command(self):
        print("command")


    def GButton_163_command(self):
        print("command")


    def GButton_91_command(self):
        print("command")


    def GButton_452_command(self):
        print("command")


    def GButton_940_command(self):
        print("command")


    def GButton_611_command(self):
        print("command")


    def GButton_491_command(self):
        print("command")


    def GButton_909_command(self):
        print("command")


    def GButton_395_command(self):
        print("command")


    def GButton_819_command(self):
        print("command")


    def GButton_572_command(self):
        print("command")


    def GButton_755_command(self):
        print("command")


    def GButton_867_command(self):
        print("command")


    def GButton_606_command(self):
        print("command")


    def GButton_51_command(self):
        print("command")


    def GButton_818_command(self):
        print("command")


    def GButton_26_command(self):
        print("command")


    def GButton_755_command(self):
        print("command")


    def GButton_788_command(self):
        print("command")


    def GButton_83_command(self):
        print("command")


    def GButton_978_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
