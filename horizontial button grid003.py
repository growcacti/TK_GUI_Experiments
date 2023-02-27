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

        b592=tk.Button(root)
        b592["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b592["font"] = ft
        b592["fg"] = "#000000"
        b592["justify"] = "center"
        b592["text"] = "Button"
        b592.place(x=20,y=20,width=70,height=25)
        b592["command"] = self.b592_command

        b89=tk.Button(root)
        b89["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b89["font"] = ft
        b89["fg"] = "#000000"
        b89["justify"] = "center"
        b89["text"] = "Button"
        b89.place(x=100,y=20,width=70,height=25)
        b89["command"] = self.b89_command

        b721=tk.Button(root)
        b721["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b721["font"] = ft
        b721["fg"] = "#000000"
        b721["justify"] = "center"
        b721["text"] = "Button"
        b721.place(x=180,y=20,width=70,height=25)
        b721["command"] = self.b721_command

        b425=tk.Button(root)
        b425["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b425["font"] = ft
        b425["fg"] = "#000000"
        b425["justify"] = "center"
        b425["text"] = "Button"
        b425.place(x=260,y=20,width=70,height=25)
        b425["command"] = self.b425_command

        b818=tk.Button(root)
        b818["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b818["font"] = ft
        b818["fg"] = "#000000"
        b818["justify"] = "center"
        b818["text"] = "Button"
        b818.place(x=980,y=50,width=70,height=25)
        b818["command"] = self.b818_command

        b946=tk.Button(root)
        b946["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b946["font"] = ft
        b946["fg"] = "#000000"
        b946["justify"] = "center"
        b946["text"] = "Button"
        b946.place(x=420,y=20,width=70,height=25)
        b946["command"] = self.b946_command

        b738=tk.Button(root)
        b738["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b738["font"] = ft
        b738["fg"] = "#000000"
        b738["justify"] = "center"
        b738["text"] = "Button"
        b738.place(x=500,y=20,width=70,height=25)
        b738["command"] = self.b738_command

        b612=tk.Button(root)
        b612["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b612["font"] = ft
        b612["fg"] = "#000000"
        b612["justify"] = "center"
        b612["text"] = "Button"
        b612.place(x=580,y=20,width=70,height=25)
        b612["command"] = self.b612_command

        b43=tk.Button(root)
        b43["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b43["font"] = ft
        b43["fg"] = "#000000"
        b43["justify"] = "center"
        b43["text"] = "Button"
        b43.place(x=660,y=20,width=70,height=25)
        b43["command"] = self.b43_command

        b395=tk.Button(root)
        b395["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b395["font"] = ft
        b395["fg"] = "#000000"
        b395["justify"] = "center"
        b395["text"] = "Button"
        b395.place(x=660,y=50,width=70,height=25)
        b395["command"] = self.b395_command

        b92=tk.Button(root)
        b92["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b92["font"] = ft
        b92["fg"] = "#000000"
        b92["justify"] = "center"
        b92["text"] = "Button"
        b92.place(x=740,y=20,width=70,height=25)
        b92["command"] = self.b92_command

        b459=tk.Button(root)
        b459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b459["font"] = ft
        b459["fg"] = "#000000"
        b459["justify"] = "center"
        b459["text"] = "Button"
        b459.place(x=100,y=50,width=70,height=25)
        b459["command"] = self.b459_command

        b163=tk.Button(root)
        b163["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b163["font"] = ft
        b163["fg"] = "#000000"
        b163["justify"] = "center"
        b163["text"] = "Button"
        b163.place(x=180,y=50,width=70,height=25)
        b163["command"] = self.b163_command

        b91=tk.Button(root)
        b91["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b91["font"] = ft
        b91["fg"] = "#000000"
        b91["justify"] = "center"
        b91["text"] = "Button"
        b91.place(x=260,y=50,width=70,height=25)
        b91["command"] = self.b91_command

        b452=tk.Button(root)
        b452["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b452["font"] = ft
        b452["fg"] = "#000000"
        b452["justify"] = "center"
        b452["text"] = "Button"
        b452.place(x=20,y=50,width=70,height=25)
        b452["command"] = self.b452_command

        b940=tk.Button(root)
        b940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b940["font"] = ft
        b940["fg"] = "#000000"
        b940["justify"] = "center"
        b940["text"] = "Button"
        b940.place(x=340,y=50,width=70,height=25)
        b940["command"] = self.b940_command

        b611=tk.Button(root)
        b611["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b611["font"] = ft
        b611["fg"] = "#000000"
        b611["justify"] = "center"
        b611["text"] = "Button"
        b611.place(x=420,y=50,width=70,height=25)
        b611["command"] = self.b611_command

        b491=tk.Button(root)
        b491["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b491["font"] = ft
        b491["fg"] = "#000000"
        b491["justify"] = "center"
        b491["text"] = "Button"
        b491.place(x=500,y=50,width=70,height=25)
        b491["command"] = self.b491_command

        b909=tk.Button(root)
        b909["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b909["font"] = ft
        b909["fg"] = "#000000"
        b909["justify"] = "center"
        b909["text"] = "Button"
        b909.place(x=580,y=50,width=70,height=25)
        b909["command"] = self.b909_command

        b395=tk.Button(root)
        b395["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b395["font"] = ft
        b395["fg"] = "#000000"
        b395["justify"] = "center"
        b395["text"] = "Button"
        b395.place(x=660,y=50,width=70,height=25)
        b395["command"] = self.b395_command

        b819=tk.Button(root)
        b819["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b819["font"] = ft
        b819["fg"] = "#000000"
        b819["justify"] = "center"
        b819["text"] = "Button"
        b819.place(x=740,y=50,width=70,height=25)
        b819["command"] = self.b819_command

        b572=tk.Button(root)
        b572["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b572["font"] = ft
        b572["fg"] = "#000000"
        b572["justify"] = "center"
        b572["text"] = "Button"
        b572.place(x=820,y=20,width=70,height=25)
        b572["command"] = self.b572_command

        b755=tk.Button(root)
        b755["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b755["font"] = ft
        b755["fg"] = "#000000"
        b755["justify"] = "center"
        b755["text"] = "Button"
        b755.place(x=1060,y=50,width=70,height=25)
        b755["command"] = self.b755_command

        b867=tk.Button(root)
        b867["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b867["font"] = ft
        b867["fg"] = "#000000"
        b867["justify"] = "center"
        b867["text"] = "Button"
        b867.place(x=900,y=20,width=70,height=25)
        b867["command"] = self.b867_command

        b606=tk.Button(root)
        b606["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b606["font"] = ft
        b606["fg"] = "#000000"
        b606["justify"] = "center"
        b606["text"] = "Button"
        b606.place(x=900,y=50,width=70,height=25)
        b606["command"] = self.b606_command

        b51=tk.Button(root)
        b51["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b51["font"] = ft
        b51["fg"] = "#000000"
        b51["justify"] = "center"
        b51["text"] = "Button"
        b51.place(x=980,y=20,width=70,height=25)
        b51["command"] = self.b51_command

        b818=tk.Button(root)
        b818["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b818["font"] = ft
        b818["fg"] = "#000000"
        b818["justify"] = "center"
        b818["text"] = "Button"
        b818.place(x=980,y=50,width=70,height=25)
        b818["command"] = self.b818_command

        b26=tk.Button(root)
        b26["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b26["font"] = ft
        b26["fg"] = "#000000"
        b26["justify"] = "center"
        b26["text"] = "Button"
        b26.place(x=1060,y=20,width=70,height=25)
        b26["command"] = self.b26_command

        b755=tk.Button(root)
        b755["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b755["font"] = ft
        b755["fg"] = "#000000"
        b755["justify"] = "center"
        b755["text"] = "Button"
        b755.place(x=1060,y=50,width=70,height=25)
        b755["command"] = self.b755_command

        b788=tk.Button(root)
        b788["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b788["font"] = ft
        b788["fg"] = "#000000"
        b788["justify"] = "center"
        b788["text"] = "Button"
        b788.place(x=1140,y=20,width=70,height=25)
        b788["command"] = self.b788_command

        b83=tk.Button(root)
        b83["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b83["font"] = ft
        b83["fg"] = "#000000"
        b83["justify"] = "center"
        b83["text"] = "Button"
        b83.place(x=1220,y=20,width=70,height=25)
        b83["command"] = self.b83_command

        b978=tk.Button(root)
        b978["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b978["font"] = ft
        b978["fg"] = "#000000"
        b978["justify"] = "center"
        b978["text"] = "Button"
        b978.place(x=1220,y=50,width=70,height=25)
        b978["command"] = self.b978_command

    def b592_command(self):
        print("command")


    def b89_command(self):
        print("command")


    def b721_command(self):
        print("command")


    def b425_command(self):
        print("command")


    def b818_command(self):
        print("command")


    def b946_command(self):
        print("command")


    def b738_command(self):
        print("command")


    def b612_command(self):
        print("command")


    def b43_command(self):
        print("command")


    def b395_command(self):
        print("command")


    def b92_command(self):
        print("command")


    def b459_command(self):
        print("command")


    def b163_command(self):
        print("command")


    def b91_command(self):
        print("command")


    def b452_command(self):
        print("command")


    def b940_command(self):
        print("command")


    def b611_command(self):
        print("command")


    def b491_command(self):
        print("command")


    def b909_command(self):
        print("command")


    def b395_command(self):
        print("command")


    def b819_command(self):
        print("command")


    def b572_command(self):
        print("command")


    def b755_command(self):
        print("command")


    def b867_command(self):
        print("command")


    def b606_command(self):
        print("command")


    def b51_command(self):
        print("command")


    def b818_command(self):
        print("command")


    def b26_command(self):
        print("command")


    def b755_command(self):
        print("command")


    def b788_command(self):
        print("command")


    def b83_command(self):
        print("command")


    def b978_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
