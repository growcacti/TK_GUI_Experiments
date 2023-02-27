import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1680
        height=885
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_334=tk.Button(root)
        GButton_334["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_334["font"] = ft
        GButton_334["fg"] = "#000000"
        GButton_334["justify"] = "center"
        GButton_334["text"] = "Button"
        GButton_334.place(x=10,y=130,width=70,height=25)
        GButton_334["command"] = self.GButton_334_command

        GButton_734=tk.Button(root)
        GButton_734["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_734["font"] = ft
        GButton_734["fg"] = "#000000"
        GButton_734["justify"] = "center"
        GButton_734["text"] = "Button"
        GButton_734.place(x=10,y=170,width=70,height=25)
        GButton_734["command"] = self.GButton_734_command

        GButton_374=tk.Button(root)
        GButton_374["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_374["font"] = ft
        GButton_374["fg"] = "#000000"
        GButton_374["justify"] = "center"
        GButton_374["text"] = "Button"
        GButton_374.place(x=10,y=210,width=70,height=25)
        GButton_374["command"] = self.GButton_374_command

        GButton_141=tk.Button(root)
        GButton_141["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_141["font"] = ft
        GButton_141["fg"] = "#000000"
        GButton_141["justify"] = "center"
        GButton_141["text"] = "Button"
        GButton_141.place(x=10,y=290,width=70,height=25)
        GButton_141["command"] = self.GButton_141_command

        GButton_657=tk.Button(root)
        GButton_657["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_657["font"] = ft
        GButton_657["fg"] = "#000000"
        GButton_657["justify"] = "center"
        GButton_657["text"] = "Button"
        GButton_657.place(x=10,y=250,width=70,height=25)
        GButton_657["command"] = self.GButton_657_command

        GButton_968=tk.Button(root)
        GButton_968["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_968["font"] = ft
        GButton_968["fg"] = "#000000"
        GButton_968["justify"] = "center"
        GButton_968["text"] = "Button"
        GButton_968.place(x=30,y=20,width=70,height=25)
        GButton_968["command"] = self.GButton_968_command

        GButton_56=tk.Button(root)
        GButton_56["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_56["font"] = ft
        GButton_56["fg"] = "#000000"
        GButton_56["justify"] = "center"
        GButton_56["text"] = "Button"
        GButton_56.place(x=110,y=20,width=70,height=25)
        GButton_56["command"] = self.GButton_56_command

        GButton_872=tk.Button(root)
        GButton_872["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_872["font"] = ft
        GButton_872["fg"] = "#000000"
        GButton_872["justify"] = "center"
        GButton_872["text"] = "Button"
        GButton_872.place(x=190,y=20,width=70,height=25)
        GButton_872["command"] = self.GButton_872_command

        GButton_992=tk.Button(root)
        GButton_992["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_992["font"] = ft
        GButton_992["fg"] = "#000000"
        GButton_992["justify"] = "center"
        GButton_992["text"] = "Button"
        GButton_992.place(x=270,y=20,width=70,height=25)
        GButton_992["command"] = self.GButton_992_command

        GButton_975=tk.Button(root)
        GButton_975["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_975["font"] = ft
        GButton_975["fg"] = "#000000"
        GButton_975["justify"] = "center"
        GButton_975["text"] = "Button"
        GButton_975.place(x=350,y=20,width=70,height=25)
        GButton_975["command"] = self.GButton_975_command

        GButton_977=tk.Button(root)
        GButton_977["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_977["font"] = ft
        GButton_977["fg"] = "#000000"
        GButton_977["justify"] = "center"
        GButton_977["text"] = "Button"
        GButton_977.place(x=430,y=20,width=70,height=25)
        GButton_977["command"] = self.GButton_977_command

        GButton_752=tk.Button(root)
        GButton_752["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_752["font"] = ft
        GButton_752["fg"] = "#000000"
        GButton_752["justify"] = "center"
        GButton_752["text"] = "Button"
        GButton_752.place(x=510,y=20,width=70,height=25)
        GButton_752["command"] = self.GButton_752_command

        GButton_888=tk.Button(root)
        GButton_888["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_888["font"] = ft
        GButton_888["fg"] = "#000000"
        GButton_888["justify"] = "center"
        GButton_888["text"] = "Button"
        GButton_888.place(x=10,y=90,width=70,height=25)
        GButton_888["command"] = self.GButton_888_command

        GButton_185=tk.Button(root)
        GButton_185["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_185["font"] = ft
        GButton_185["fg"] = "#000000"
        GButton_185["justify"] = "center"
        GButton_185["text"] = "Button"
        GButton_185.place(x=10,y=330,width=70,height=25)
        GButton_185["command"] = self.GButton_185_command

        GButton_257=tk.Button(root)
        GButton_257["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_257["font"] = ft
        GButton_257["fg"] = "#000000"
        GButton_257["justify"] = "center"
        GButton_257["text"] = "Button"
        GButton_257.place(x=10,y=370,width=70,height=25)
        GButton_257["command"] = self.GButton_257_command

        GButton_96=tk.Button(root)
        GButton_96["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_96["font"] = ft
        GButton_96["fg"] = "#000000"
        GButton_96["justify"] = "center"
        GButton_96["text"] = "Button"
        GButton_96.place(x=590,y=20,width=70,height=25)
        GButton_96["command"] = self.GButton_96_command

        GButton_616=tk.Button(root)
        GButton_616["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_616["font"] = ft
        GButton_616["fg"] = "#000000"
        GButton_616["justify"] = "center"
        GButton_616["text"] = "Button"
        GButton_616.place(x=670,y=20,width=70,height=25)
        GButton_616["command"] = self.GButton_616_command

        GButton_64=tk.Button(root)
        GButton_64["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_64["font"] = ft
        GButton_64["fg"] = "#000000"
        GButton_64["justify"] = "center"
        GButton_64["text"] = "Button"
        GButton_64.place(x=510,y=50,width=70,height=25)
        GButton_64["command"] = self.GButton_64_command

        GButton_864=tk.Button(root)
        GButton_864["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_864["font"] = ft
        GButton_864["fg"] = "#000000"
        GButton_864["justify"] = "center"
        GButton_864["text"] = "Button"
        GButton_864.place(x=750,y=50,width=70,height=25)
        GButton_864["command"] = self.GButton_864_command

        GButton_368=tk.Button(root)
        GButton_368["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_368["font"] = ft
        GButton_368["fg"] = "#000000"
        GButton_368["justify"] = "center"
        GButton_368["text"] = "Button"
        GButton_368.place(x=10,y=440,width=70,height=25)
        GButton_368["command"] = self.GButton_368_command

        GButton_889=tk.Button(root)
        GButton_889["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_889["font"] = ft
        GButton_889["fg"] = "#000000"
        GButton_889["justify"] = "center"
        GButton_889["text"] = "Button"
        GButton_889.place(x=30,y=50,width=70,height=25)
        GButton_889["command"] = self.GButton_889_command

        GButton_168=tk.Button(root)
        GButton_168["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_168["font"] = ft
        GButton_168["fg"] = "#000000"
        GButton_168["justify"] = "center"
        GButton_168["text"] = "Button"
        GButton_168.place(x=110,y=50,width=70,height=25)
        GButton_168["command"] = self.GButton_168_command

        GButton_800=tk.Button(root)
        GButton_800["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_800["font"] = ft
        GButton_800["fg"] = "#000000"
        GButton_800["justify"] = "center"
        GButton_800["text"] = "Button"
        GButton_800.place(x=190,y=50,width=70,height=25)
        GButton_800["command"] = self.GButton_800_command

        GButton_800=tk.Button(root)
        GButton_800["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_800["font"] = ft
        GButton_800["fg"] = "#000000"
        GButton_800["justify"] = "center"
        GButton_800["text"] = "Button"
        GButton_800.place(x=190,y=50,width=70,height=25)
        GButton_800["command"] = self.GButton_800_command

        GButton_369=tk.Button(root)
        GButton_369["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_369["font"] = ft
        GButton_369["fg"] = "#000000"
        GButton_369["justify"] = "center"
        GButton_369["text"] = "Button"
        GButton_369.place(x=270,y=50,width=70,height=25)
        GButton_369["command"] = self.GButton_369_command

        GButton_321=tk.Button(root)
        GButton_321["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "Button"
        GButton_321.place(x=350,y=50,width=70,height=25)
        GButton_321["command"] = self.GButton_321_command

        GButton_833=tk.Button(root)
        GButton_833["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_833["font"] = ft
        GButton_833["fg"] = "#000000"
        GButton_833["justify"] = "center"
        GButton_833["text"] = "Button"
        GButton_833.place(x=430,y=50,width=70,height=25)
        GButton_833["command"] = self.GButton_833_command

        GButton_64=tk.Button(root)
        GButton_64["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_64["font"] = ft
        GButton_64["fg"] = "#000000"
        GButton_64["justify"] = "center"
        GButton_64["text"] = "Button"
        GButton_64.place(x=510,y=50,width=70,height=25)
        GButton_64["command"] = self.GButton_64_command

        GButton_24=tk.Button(root)
        GButton_24["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_24["font"] = ft
        GButton_24["fg"] = "#000000"
        GButton_24["justify"] = "center"
        GButton_24["text"] = "Button"
        GButton_24.place(x=590,y=50,width=70,height=25)
        GButton_24["command"] = self.GButton_24_command

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Button"
        GButton_265.place(x=670,y=50,width=70,height=25)
        GButton_265["command"] = self.GButton_265_command

        GLineEdit_418=tk.Entry(root)
        GLineEdit_418["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_418["font"] = ft
        GLineEdit_418["fg"] = "#333333"
        GLineEdit_418["justify"] = "center"
        GLineEdit_418["text"] = "Entry"
        GLineEdit_418.place(x=120,y=100,width=1544,height=715)

        GRadio_738=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_738["font"] = ft
        GRadio_738["fg"] = "#333333"
        GRadio_738["justify"] = "center"
        GRadio_738["text"] = "RadioButton"
        GRadio_738.place(x=940,y=30,width=85,height=25)
        GRadio_738["command"] = self.GRadio_738_command

        GRadio_82=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_82["font"] = ft
        GRadio_82["fg"] = "#333333"
        GRadio_82["justify"] = "center"
        GRadio_82["text"] = "RadioButton"
        GRadio_82.place(x=1110,y=30,width=85,height=25)
        GRadio_82["command"] = self.GRadio_82_command

        GRadio_649=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_649["font"] = ft
        GRadio_649["fg"] = "#333333"
        GRadio_649["justify"] = "center"
        GRadio_649["text"] = "RadioButton"
        GRadio_649.place(x=1250,y=30,width=85,height=25)
        GRadio_649["command"] = self.GRadio_649_command

    def GButton_334_command(self):
        print("command")


    def GButton_734_command(self):
        print("command")


    def GButton_374_command(self):
        print("command")


    def GButton_141_command(self):
        print("command")


    def GButton_657_command(self):
        print("command")


    def GButton_968_command(self):
        print("command")


    def GButton_56_command(self):
        print("command")


    def GButton_872_command(self):
        print("command")


    def GButton_992_command(self):
        print("command")


    def GButton_975_command(self):
        print("command")


    def GButton_977_command(self):
        print("command")


    def GButton_752_command(self):
        print("command")


    def GButton_888_command(self):
        print("command")


    def GButton_185_command(self):
        print("command")


    def GButton_257_command(self):
        print("command")


    def GButton_96_command(self):
        print("command")


    def GButton_616_command(self):
        print("command")


    def GButton_64_command(self):
        print("command")


    def GButton_864_command(self):
        print("command")


    def GButton_368_command(self):
        print("command")


    def GButton_889_command(self):
        print("command")


    def GButton_168_command(self):
        print("command")


    def GButton_800_command(self):
        print("command")


    def GButton_800_command(self):
        print("command")


    def GButton_369_command(self):
        print("command")


    def GButton_321_command(self):
        print("command")


    def GButton_833_command(self):
        print("command")


    def GButton_64_command(self):
        print("command")


    def GButton_24_command(self):
        print("command")


    def GButton_265_command(self):
        print("command")


    def GRadio_738_command(self):
        print("command")


    def GRadio_82_command(self):
        print("command")


    def GRadio_649_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
