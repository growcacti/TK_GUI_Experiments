import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_348=tk.Entry(root)
        GLineEdit_348["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_348["font"] = ft
        GLineEdit_348["fg"] = "#333333"
        GLineEdit_348["justify"] = "center"
        GLineEdit_348["text"] = "Entry"
        GLineEdit_348.place(x=100,y=50,width=70,height=25)

        GCheckBox_28=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_28["font"] = ft
        GCheckBox_28["fg"] = "#333333"
        GCheckBox_28["justify"] = "center"
        GCheckBox_28["text"] = "CheckBox"
        GCheckBox_28.place(x=20,y=50,width=70,height=25)
        GCheckBox_28["offvalue"] = "0"
        GCheckBox_28["onvalue"] = "1"
        GCheckBox_28["command"] = self.GCheckBox_28_command

        GLineEdit_131=tk.Entry(root)
        GLineEdit_131["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_131["font"] = ft
        GLineEdit_131["fg"] = "#333333"
        GLineEdit_131["justify"] = "center"
        GLineEdit_131["text"] = "Entry"
        GLineEdit_131.place(x=100,y=90,width=70,height=25)

        GCheckBox_261=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_261["font"] = ft
        GCheckBox_261["fg"] = "#333333"
        GCheckBox_261["justify"] = "center"
        GCheckBox_261["text"] = "CheckBox"
        GCheckBox_261.place(x=20,y=90,width=70,height=25)
        GCheckBox_261["offvalue"] = "0"
        GCheckBox_261["onvalue"] = "1"
        GCheckBox_261["command"] = self.GCheckBox_261_command

        GCheckBox_900=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_900["font"] = ft
        GCheckBox_900["fg"] = "#333333"
        GCheckBox_900["justify"] = "center"
        GCheckBox_900["text"] = "CheckBox"
        GCheckBox_900.place(x=220,y=220,width=70,height=25)
        GCheckBox_900["offvalue"] = "0"
        GCheckBox_900["onvalue"] = "1"
        GCheckBox_900["command"] = self.GCheckBox_900_command

        GLineEdit_836=tk.Entry(root)
        GLineEdit_836["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_836["font"] = ft
        GLineEdit_836["fg"] = "#333333"
        GLineEdit_836["justify"] = "center"
        GLineEdit_836["text"] = "Entry"
        GLineEdit_836.place(x=100,y=130,width=70,height=25)

        GCheckBox_4=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_4["font"] = ft
        GCheckBox_4["fg"] = "#333333"
        GCheckBox_4["justify"] = "center"
        GCheckBox_4["text"] = "CheckBox"
        GCheckBox_4.place(x=20,y=220,width=70,height=25)
        GCheckBox_4["offvalue"] = "0"
        GCheckBox_4["onvalue"] = "1"
        GCheckBox_4["command"] = self.GCheckBox_4_command

        GCheckBox_971=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_971["font"] = ft
        GCheckBox_971["fg"] = "#333333"
        GCheckBox_971["justify"] = "center"
        GCheckBox_971["text"] = "CheckBox"
        GCheckBox_971.place(x=20,y=250,width=70,height=25)
        GCheckBox_971["offvalue"] = "0"
        GCheckBox_971["onvalue"] = "1"
        GCheckBox_971["command"] = self.GCheckBox_971_command

        GCheckBox_379=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_379["font"] = ft
        GCheckBox_379["fg"] = "#333333"
        GCheckBox_379["justify"] = "center"
        GCheckBox_379["text"] = "CheckBox"
        GCheckBox_379.place(x=20,y=280,width=70,height=25)
        GCheckBox_379["offvalue"] = "0"
        GCheckBox_379["onvalue"] = "1"
        GCheckBox_379["command"] = self.GCheckBox_379_command

        GLineEdit_324=tk.Entry(root)
        GLineEdit_324["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_324["font"] = ft
        GLineEdit_324["fg"] = "#333333"
        GLineEdit_324["justify"] = "center"
        GLineEdit_324["text"] = "Entry"
        GLineEdit_324.place(x=100,y=220,width=70,height=25)

        GLineEdit_91=tk.Entry(root)
        GLineEdit_91["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_91["font"] = ft
        GLineEdit_91["fg"] = "#333333"
        GLineEdit_91["justify"] = "center"
        GLineEdit_91["text"] = "Entry"
        GLineEdit_91.place(x=100,y=260,width=70,height=25)

        GLineEdit_460=tk.Entry(root)
        GLineEdit_460["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_460["font"] = ft
        GLineEdit_460["fg"] = "#333333"
        GLineEdit_460["justify"] = "center"
        GLineEdit_460["text"] = "Entry"
        GLineEdit_460.place(x=100,y=300,width=70,height=25)

        GCheckBox_133=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_133["font"] = ft
        GCheckBox_133["fg"] = "#333333"
        GCheckBox_133["justify"] = "center"
        GCheckBox_133["text"] = "CheckBox"
        GCheckBox_133.place(x=250,y=60,width=70,height=25)
        GCheckBox_133["offvalue"] = "0"
        GCheckBox_133["onvalue"] = "1"
        GCheckBox_133["command"] = self.GCheckBox_133_command

        GCheckBox_300=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_300["font"] = ft
        GCheckBox_300["fg"] = "#333333"
        GCheckBox_300["justify"] = "center"
        GCheckBox_300["text"] = "CheckBox"
        GCheckBox_300.place(x=250,y=100,width=70,height=25)
        GCheckBox_300["offvalue"] = "0"
        GCheckBox_300["onvalue"] = "1"
        GCheckBox_300["command"] = self.GCheckBox_300_command

        GCheckBox_854=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_854["font"] = ft
        GCheckBox_854["fg"] = "#333333"
        GCheckBox_854["justify"] = "center"
        GCheckBox_854["text"] = "CheckBox"
        GCheckBox_854.place(x=250,y=130,width=70,height=25)
        GCheckBox_854["offvalue"] = "0"
        GCheckBox_854["onvalue"] = "1"
        GCheckBox_854["command"] = self.GCheckBox_854_command

        GButton_709=tk.Button(root)
        GButton_709["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_709["font"] = ft
        GButton_709["fg"] = "#000000"
        GButton_709["justify"] = "center"
        GButton_709["text"] = "Button"
        GButton_709.place(x=70,y=170,width=70,height=25)
        GButton_709["command"] = self.GButton_709_command

        GButton_405=tk.Button(root)
        GButton_405["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_405["font"] = ft
        GButton_405["fg"] = "#000000"
        GButton_405["justify"] = "center"
        GButton_405["text"] = "Button"
        GButton_405.place(x=310,y=170,width=70,height=25)
        GButton_405["command"] = self.GButton_405_command

        GButton_12=tk.Button(root)
        GButton_12["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_12["font"] = ft
        GButton_12["fg"] = "#000000"
        GButton_12["justify"] = "center"
        GButton_12["text"] = "Button"
        GButton_12.place(x=70,y=340,width=70,height=25)
        GButton_12["command"] = self.GButton_12_command

        GLineEdit_180=tk.Entry(root)
        GLineEdit_180["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_180["font"] = ft
        GLineEdit_180["fg"] = "#333333"
        GLineEdit_180["justify"] = "center"
        GLineEdit_180["text"] = "Entry"
        GLineEdit_180.place(x=350,y=50,width=70,height=25)

        GLineEdit_107=tk.Entry(root)
        GLineEdit_107["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_107["font"] = ft
        GLineEdit_107["fg"] = "#333333"
        GLineEdit_107["justify"] = "center"
        GLineEdit_107["text"] = "Entry"
        GLineEdit_107.place(x=350,y=90,width=70,height=25)

        GLineEdit_932=tk.Entry(root)
        GLineEdit_932["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_932["font"] = ft
        GLineEdit_932["fg"] = "#333333"
        GLineEdit_932["justify"] = "center"
        GLineEdit_932["text"] = "Entry"
        GLineEdit_932.place(x=350,y=130,width=70,height=25)

        GCheckBox_302=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_302["font"] = ft
        GCheckBox_302["fg"] = "#333333"
        GCheckBox_302["justify"] = "center"
        GCheckBox_302["text"] = "CheckBox"
        GCheckBox_302.place(x=220,y=260,width=70,height=25)
        GCheckBox_302["offvalue"] = "0"
        GCheckBox_302["onvalue"] = "1"
        GCheckBox_302["command"] = self.GCheckBox_302_command

        GCheckBox_789=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_789["font"] = ft
        GCheckBox_789["fg"] = "#333333"
        GCheckBox_789["justify"] = "center"
        GCheckBox_789["text"] = "CheckBox"
        GCheckBox_789.place(x=220,y=300,width=70,height=25)
        GCheckBox_789["offvalue"] = "0"
        GCheckBox_789["onvalue"] = "1"
        GCheckBox_789["command"] = self.GCheckBox_789_command

        GLineEdit_222=tk.Entry(root)
        GLineEdit_222["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_222["font"] = ft
        GLineEdit_222["fg"] = "#333333"
        GLineEdit_222["justify"] = "center"
        GLineEdit_222["text"] = "Entry"
        GLineEdit_222.place(x=360,y=220,width=70,height=25)

        GLineEdit_333=tk.Entry(root)
        GLineEdit_333["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_333["font"] = ft
        GLineEdit_333["fg"] = "#333333"
        GLineEdit_333["justify"] = "center"
        GLineEdit_333["text"] = "Entry"
        GLineEdit_333.place(x=360,y=260,width=70,height=25)

        GLineEdit_653=tk.Entry(root)
        GLineEdit_653["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_653["font"] = ft
        GLineEdit_653["fg"] = "#333333"
        GLineEdit_653["justify"] = "center"
        GLineEdit_653["text"] = "Entry"
        GLineEdit_653.place(x=360,y=300,width=70,height=25)

        GButton_454=tk.Button(root)
        GButton_454["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_454["font"] = ft
        GButton_454["fg"] = "#000000"
        GButton_454["justify"] = "center"
        GButton_454["text"] = "Button"
        GButton_454.place(x=280,y=340,width=70,height=25)
        GButton_454["command"] = self.GButton_454_command

        GButton_686=tk.Button(root)
        GButton_686["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_686["font"] = ft
        GButton_686["fg"] = "#000000"
        GButton_686["justify"] = "center"
        GButton_686["text"] = "Button"
        GButton_686.place(x=10,y=440,width=70,height=25)
        GButton_686["command"] = self.GButton_686_command

        GButton_437=tk.Button(root)
        GButton_437["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_437["font"] = ft
        GButton_437["fg"] = "#000000"
        GButton_437["justify"] = "center"
        GButton_437["text"] = "Button"
        GButton_437.place(x=100,y=440,width=70,height=25)
        GButton_437["command"] = self.GButton_437_command

        GButton_350=tk.Button(root)
        GButton_350["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_350["font"] = ft
        GButton_350["fg"] = "#000000"
        GButton_350["justify"] = "center"
        GButton_350["text"] = "Button"
        GButton_350.place(x=180,y=440,width=70,height=25)
        GButton_350["command"] = self.GButton_350_command

        GButton_76=tk.Button(root)
        GButton_76["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_76["font"] = ft
        GButton_76["fg"] = "#000000"
        GButton_76["justify"] = "center"
        GButton_76["text"] = "Button"
        GButton_76.place(x=270,y=440,width=70,height=25)
        GButton_76["command"] = self.GButton_76_command

        GButton_462=tk.Button(root)
        GButton_462["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_462["font"] = ft
        GButton_462["fg"] = "#000000"
        GButton_462["justify"] = "center"
        GButton_462["text"] = "Button"
        GButton_462.place(x=360,y=440,width=70,height=25)
        GButton_462["command"] = self.GButton_462_command

        GButton_799=tk.Button(root)
        GButton_799["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_799["font"] = ft
        GButton_799["fg"] = "#000000"
        GButton_799["justify"] = "center"
        GButton_799["text"] = "Button"
        GButton_799.place(x=440,y=440,width=70,height=25)
        GButton_799["command"] = self.GButton_799_command

    def GCheckBox_28_command(self):
        print("command")


    def GCheckBox_261_command(self):
        print("command")


    def GCheckBox_900_command(self):
        print("command")


    def GCheckBox_4_command(self):
        print("command")


    def GCheckBox_971_command(self):
        print("command")


    def GCheckBox_379_command(self):
        print("command")


    def GCheckBox_133_command(self):
        print("command")


    def GCheckBox_300_command(self):
        print("command")


    def GCheckBox_854_command(self):
        print("command")


    def GButton_709_command(self):
        print("command")


    def GButton_405_command(self):
        print("command")


    def GButton_12_command(self):
        print("command")


    def GCheckBox_302_command(self):
        print("command")


    def GCheckBox_789_command(self):
        print("command")


    def GButton_454_command(self):
        print("command")


    def GButton_686_command(self):
        print("command")


    def GButton_437_command(self):
        print("command")


    def GButton_350_command(self):
        print("command")


    def GButton_76_command(self):
        print("command")


    def GButton_462_command(self):
        print("command")


    def GButton_799_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
