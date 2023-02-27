import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=159
        height=518
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        b537=tk.Button(root)
        b537["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b537["font"] = ft
        b537["fg"] = "#000000"
        b537["justify"] = "center"
        b537["text"] = "Button"
        b537.place(x=0,y=30,width=70,height=25)
        b537["command"] = self.b537_command

        b387=tk.Button(root)
        b387["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b387["font"] = ft
        b387["fg"] = "#000000"
        b387["justify"] = "center"
        b387["text"] = "Button"
        b387.place(x=80,y=30,width=70,height=25)
        b387["command"] = self.b387_command

        b721=tk.Button(root)
        b721["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b721["font"] = ft
        b721["fg"] = "#000000"
        b721["justify"] = "center"
        b721["text"] = "Button"
        b721.place(x=0,y=240,width=70,height=25)
        b721["command"] = self.b721_command

        b385=tk.Button(root)
        b385["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b385["font"] = ft
        b385["fg"] = "#000000"
        b385["justify"] = "center"
        b385["text"] = "Button"
        b385.place(x=80,y=450,width=70,height=25)
        b385["command"] = self.b385_command

        b329=tk.Button(root)
        b329["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b329["font"] = ft
        b329["fg"] = "#000000"
        b329["justify"] = "center"
        b329["text"] = "Button"
        b329.place(x=0,y=60,width=70,height=25)
        b329["command"] = self.b329_command

        b18=tk.Button(root)
        b18["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b18["font"] = ft
        b18["fg"] = "#000000"
        b18["justify"] = "center"
        b18["text"] = "Button"
        b18.place(x=80,y=60,width=70,height=25)
        b18["command"] = self.b18_command

        b522=tk.Button(root)
        b522["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b522["font"] = ft
        b522["fg"] = "#000000"
        b522["justify"] = "center"
        b522["text"] = "Button"
        b522.place(x=80,y=270,width=70,height=25)
        b522["command"] = self.b522_command

        b826=tk.Button(root)
        b826["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b826["font"] = ft
        b826["fg"] = "#000000"
        b826["justify"] = "center"
        b826["text"] = "Button"
        b826.place(x=0,y=420,width=70,height=25)
        b826["command"] = self.b826_command

        b737=tk.Button(root)
        b737["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b737["font"] = ft
        b737["fg"] = "#000000"
        b737["justify"] = "center"
        b737["text"] = "Button"
        b737.place(x=0,y=120,width=70,height=25)
        b737["command"] = self.b737_command

        b98=tk.Button(root)
        b98["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b98["font"] = ft
        b98["fg"] = "#000000"
        b98["justify"] = "center"
        b98["text"] = "Button"
        b98.place(x=80,y=150,width=70,height=25)
        b98["command"] = self.b98_command

        b321=tk.Button(root)
        b321["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b321["font"] = ft
        b321["fg"] = "#000000"
        b321["justify"] = "center"
        b321["text"] = "Button"
        b321.place(x=0,y=330,width=70,height=25)
        b321["command"] = self.b321_command

        b164=tk.Button(root)
        b164["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b164["font"] = ft
        b164["fg"] = "#000000"
        b164["justify"] = "center"
        b164["text"] = "Button"
        b164.place(x=80,y=420,width=70,height=25)
        b164["command"] = self.b164_command

        b459=tk.Button(root)
        b459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b459["font"] = ft
        b459["fg"] = "#000000"
        b459["justify"] = "center"
        b459["text"] = "Button"
        b459.place(x=0,y=150,width=70,height=25)
        b459["command"] = self.b459_command

        b817=tk.Button(root)
        b817["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b817["font"] = ft
        b817["fg"] = "#000000"
        b817["justify"] = "center"
        b817["text"] = "Button"
        b817.place(x=0,y=90,width=70,height=25)
        b817["command"] = self.b817_command

        b74=tk.Button(root)
        b74["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b74["font"] = ft
        b74["fg"] = "#000000"
        b74["justify"] = "center"
        b74["text"] = "Button"
        b74.place(x=80,y=210,width=70,height=25)
        b74["command"] = self.b74_command

        b75=tk.Button(root)
        b75["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b75["font"] = ft
        b75["fg"] = "#000000"
        b75["justify"] = "center"
        b75["text"] = "Button"
        b75.place(x=80,y=180,width=70,height=25)
        b75["command"] = self.b75_command

        b515=tk.Button(root)
        b515["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b515["font"] = ft
        b515["fg"] = "#000000"
        b515["justify"] = "center"
        b515["text"] = "Button"
        b515.place(x=80,y=300,width=70,height=25)
        b515["command"] = self.b515_command

        b834=tk.Button(root)
        b834["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b834["font"] = ft
        b834["fg"] = "#000000"
        b834["justify"] = "center"
        b834["text"] = "Button"
        b834.place(x=80,y=330,width=70,height=25)
        b834["command"] = self.b834_command

        b475=tk.Button(root)
        b475["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b475["font"] = ft
        b475["fg"] = "#000000"
        b475["justify"] = "center"
        b475["text"] = "Button"
        b475.place(x=0,y=360,width=70,height=25)
        b475["command"] = self.b475_command

        b900=tk.Button(root)
        b900["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b900["font"] = ft
        b900["fg"] = "#000000"
        b900["justify"] = "center"
        b900["text"] = "Button"
        b900.place(x=80,y=390,width=70,height=25)
        b900["command"] = self.b900_command

        b619=tk.Button(root)
        b619["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b619["font"] = ft
        b619["fg"] = "#000000"
        b619["justify"] = "center"
        b619["text"] = "Button"
        b619.place(x=0,y=210,width=70,height=25)
        b619["command"] = self.b619_command

        b418=tk.Button(root)
        b418["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b418["font"] = ft
        b418["fg"] = "#000000"
        b418["justify"] = "center"
        b418["text"] = "Button"
        b418.place(x=80,y=240,width=70,height=25)
        b418["command"] = self.b418_command

        b595=tk.Button(root)
        b595["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b595["font"] = ft
        b595["fg"] = "#000000"
        b595["justify"] = "center"
        b595["text"] = "Button"
        b595.place(x=0,y=300,width=70,height=25)
        b595["command"] = self.b595_command

        b434=tk.Button(root)
        b434["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b434["font"] = ft
        b434["fg"] = "#000000"
        b434["justify"] = "center"
        b434["text"] = "Button"
        b434.place(x=0,y=270,width=70,height=25)
        b434["command"] = self.b434_command

        b11=tk.Button(root)
        b11["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b11["font"] = ft
        b11["fg"] = "#000000"
        b11["justify"] = "center"
        b11["text"] = "Button"
        b11.place(x=80,y=90,width=70,height=25)
        b11["command"] = self.b11_command

        b940=tk.Button(root)
        b940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b940["font"] = ft
        b940["fg"] = "#000000"
        b940["justify"] = "center"
        b940["text"] = "Button"
        b940.place(x=80,y=360,width=70,height=25)
        b940["command"] = self.b940_command

        b338=tk.Button(root)
        b338["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b338["font"] = ft
        b338["fg"] = "#000000"
        b338["justify"] = "center"
        b338["text"] = "Button"
        b338.place(x=0,y=390,width=70,height=25)
        b338["command"] = self.b338_command

        b396=tk.Button(root)
        b396["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b396["font"] = ft
        b396["fg"] = "#000000"
        b396["justify"] = "center"
        b396["text"] = "Button"
        b396.place(x=0,y=450,width=70,height=25)
        b396["command"] = self.b396_command

        b530=tk.Button(root)
        b530["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b530["font"] = ft
        b530["fg"] = "#000000"
        b530["justify"] = "center"
        b530["text"] = "Button"
        b530.place(x=80,y=480,width=70,height=25)
        b530["command"] = self.b530_command

        b139=tk.Button(root)
        b139["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b139["font"] = ft
        b139["fg"] = "#000000"
        b139["justify"] = "center"
        b139["text"] = "Button"
        b139.place(x=0,y=480,width=70,height=25)
        b139["command"] = self.b139_command

        b91=tk.Button(root)
        b91["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b91["font"] = ft
        b91["fg"] = "#000000"
        b91["justify"] = "center"
        b91["text"] = "Button"
        b91.place(x=0,y=0,width=70,height=25)
        b91["command"] = self.b91_command

        b291=tk.Button(root)
        b291["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b291["font"] = ft
        b291["fg"] = "#000000"
        b291["justify"] = "center"
        b291["text"] = "Button"
        b291.place(x=80,y=120,width=70,height=25)
        b291["command"] = self.b291_command

        b613=tk.Button(root)
        b613["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b613["font"] = ft
        b613["fg"] = "#000000"
        b613["justify"] = "center"
        b613["text"] = "Button"
        b613.place(x=0,y=180,width=70,height=25)
        b613["command"] = self.b613_command

        b412=tk.Button(root)
        b412["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b412["font"] = ft
        b412["fg"] = "#000000"
        b412["justify"] = "center"
        b412["text"] = "Button"
        b412.place(x=80,y=0,width=70,height=25)
        b412["command"] = self.b412_command

    def b537_command(self):
        print("command")


    def b387_command(self):
        print("command")


    def b721_command(self):
        print("command")


    def b385_command(self):
        print("command")


    def b329_command(self):
        print("command")


    def b18_command(self):
        print("command")


    def b522_command(self):
        print("command")


    def b826_command(self):
        print("command")


    def b737_command(self):
        print("command")


    def b98_command(self):
        print("command")


    def b321_command(self):
        print("command")


    def b164_command(self):
        print("command")


    def b459_command(self):
        print("command")


    def b817_command(self):
        print("command")


    def b74_command(self):
        print("command")


    def b75_command(self):
        print("command")


    def b515_command(self):
        print("command")


    def b834_command(self):
        print("command")


    def b475_command(self):
        print("command")


    def b900_command(self):
        print("command")


    def b619_command(self):
        print("command")


    def b418_command(self):
        print("command")


    def b595_command(self):
        print("command")


    def b434_command(self):
        print("command")


    def b11_command(self):
        print("command")


    def b940_command(self):
        print("command")


    def b338_command(self):
        print("command")


    def b396_command(self):
        print("command")


    def b530_command(self):
        print("command")


    def b139_command(self):
        print("command")


    def b91_command(self):
        print("command")


    def b291_command(self):
        print("command")


    def b613_command(self):
        print("command")


    def b412_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
