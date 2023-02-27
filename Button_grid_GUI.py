import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=359
        height=315
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_537=tk.Button(root)
        GButton_537["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_537["font"] = ft
        GButton_537["fg"] = "#000000"
        GButton_537["justify"] = "center"
        GButton_537["text"] = "Button"
        GButton_537.place(x=50,y=20,width=70,height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_387=tk.Button(root)
        GButton_387["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_387["font"] = ft
        GButton_387["fg"] = "#000000"
        GButton_387["justify"] = "center"
        GButton_387["text"] = "Button"
        GButton_387.place(x=120,y=20,width=70,height=25)
        GButton_387["command"] = self.GButton_387_command

        GButton_721=tk.Button(root)
        GButton_721["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_721["font"] = ft
        GButton_721["fg"] = "#000000"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "Button"
        GButton_721.place(x=190,y=20,width=70,height=25)
        GButton_721["command"] = self.GButton_721_command

        GButton_385=tk.Button(root)
        GButton_385["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_385["font"] = ft
        GButton_385["fg"] = "#000000"
        GButton_385["justify"] = "center"
        GButton_385["text"] = "Button"
        GButton_385.place(x=260,y=20,width=70,height=25)
        GButton_385["command"] = self.GButton_385_command

        GButton_329=tk.Button(root)
        GButton_329["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_329["font"] = ft
        GButton_329["fg"] = "#000000"
        GButton_329["justify"] = "center"
        GButton_329["text"] = "Button"
        GButton_329.place(x=50,y=50,width=70,height=25)
        GButton_329["command"] = self.GButton_329_command

        GButton_18=tk.Button(root)
        GButton_18["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_18["font"] = ft
        GButton_18["fg"] = "#000000"
        GButton_18["justify"] = "center"
        GButton_18["text"] = "Button"
        GButton_18.place(x=120,y=50,width=70,height=25)
        GButton_18["command"] = self.GButton_18_command

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "Button"
        GButton_522.place(x=190,y=50,width=70,height=25)
        GButton_522["command"] = self.GButton_522_command

        GButton_826=tk.Button(root)
        GButton_826["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_826["font"] = ft
        GButton_826["fg"] = "#000000"
        GButton_826["justify"] = "center"
        GButton_826["text"] = "Button"
        GButton_826.place(x=260,y=50,width=70,height=25)
        GButton_826["command"] = self.GButton_826_command

        GButton_737=tk.Button(root)
        GButton_737["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Button"
        GButton_737.place(x=50,y=110,width=70,height=25)
        GButton_737["command"] = self.GButton_737_command

        GButton_98=tk.Button(root)
        GButton_98["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_98["font"] = ft
        GButton_98["fg"] = "#000000"
        GButton_98["justify"] = "center"
        GButton_98["text"] = "Button"
        GButton_98.place(x=120,y=110,width=70,height=25)
        GButton_98["command"] = self.GButton_98_command

        GButton_321=tk.Button(root)
        GButton_321["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "Button"
        GButton_321.place(x=190,y=110,width=70,height=25)
        GButton_321["command"] = self.GButton_321_command

        GButton_164=tk.Button(root)
        GButton_164["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_164["font"] = ft
        GButton_164["fg"] = "#000000"
        GButton_164["justify"] = "center"
        GButton_164["text"] = "Button"
        GButton_164.place(x=260,y=110,width=70,height=25)
        GButton_164["command"] = self.GButton_164_command

        GButton_459=tk.Button(root)
        GButton_459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#000000"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "Button"
        GButton_459.place(x=50,y=140,width=70,height=25)
        GButton_459["command"] = self.GButton_459_command

        GButton_882=tk.Button(root)
        GButton_882["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_882["font"] = ft
        GButton_882["fg"] = "#000000"
        GButton_882["justify"] = "center"
        GButton_882["text"] = "Button"
        GButton_882.place(x=50,y=170,width=70,height=25)
        GButton_882["command"] = self.GButton_882_command

        GButton_817=tk.Button(root)
        GButton_817["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_817["font"] = ft
        GButton_817["fg"] = "#000000"
        GButton_817["justify"] = "center"
        GButton_817["text"] = "Button"
        GButton_817.place(x=50,y=80,width=70,height=25)
        GButton_817["command"] = self.GButton_817_command

        GButton_74=tk.Button(root)
        GButton_74["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_74["font"] = ft
        GButton_74["fg"] = "#000000"
        GButton_74["justify"] = "center"
        GButton_74["text"] = "Button"
        GButton_74.place(x=120,y=170,width=70,height=25)
        GButton_74["command"] = self.GButton_74_command

        GButton_75=tk.Button(root)
        GButton_75["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_75["font"] = ft
        GButton_75["fg"] = "#000000"
        GButton_75["justify"] = "center"
        GButton_75["text"] = "Button"
        GButton_75.place(x=120,y=140,width=70,height=25)
        GButton_75["command"] = self.GButton_75_command

        GButton_515=tk.Button(root)
        GButton_515["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_515["font"] = ft
        GButton_515["fg"] = "#000000"
        GButton_515["justify"] = "center"
        GButton_515["text"] = "Button"
        GButton_515.place(x=190,y=170,width=70,height=25)
        GButton_515["command"] = self.GButton_515_command

        GButton_834=tk.Button(root)
        GButton_834["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_834["font"] = ft
        GButton_834["fg"] = "#000000"
        GButton_834["justify"] = "center"
        GButton_834["text"] = "Button"
        GButton_834.place(x=190,y=140,width=70,height=25)
        GButton_834["command"] = self.GButton_834_command

        GButton_475=tk.Button(root)
        GButton_475["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_475["font"] = ft
        GButton_475["fg"] = "#000000"
        GButton_475["justify"] = "center"
        GButton_475["text"] = "Button"
        GButton_475.place(x=260,y=170,width=70,height=25)
        GButton_475["command"] = self.GButton_475_command

        GButton_900=tk.Button(root)
        GButton_900["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_900["font"] = ft
        GButton_900["fg"] = "#000000"
        GButton_900["justify"] = "center"
        GButton_900["text"] = "Button"
        GButton_900.place(x=260,y=140,width=70,height=25)
        GButton_900["command"] = self.GButton_900_command

        GButton_619=tk.Button(root)
        GButton_619["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_619["font"] = ft
        GButton_619["fg"] = "#000000"
        GButton_619["justify"] = "center"
        GButton_619["text"] = "Button"
        GButton_619.place(x=50,y=200,width=70,height=25)
        GButton_619["command"] = self.GButton_619_command

        GButton_418=tk.Button(root)
        GButton_418["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_418["font"] = ft
        GButton_418["fg"] = "#000000"
        GButton_418["justify"] = "center"
        GButton_418["text"] = "Button"
        GButton_418.place(x=120,y=200,width=70,height=25)
        GButton_418["command"] = self.GButton_418_command

        GButton_595=tk.Button(root)
        GButton_595["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_595["font"] = ft
        GButton_595["fg"] = "#000000"
        GButton_595["justify"] = "center"
        GButton_595["text"] = "Button"
        GButton_595.place(x=260,y=200,width=70,height=25)
        GButton_595["command"] = self.GButton_595_command

        GButton_434=tk.Button(root)
        GButton_434["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_434["font"] = ft
        GButton_434["fg"] = "#000000"
        GButton_434["justify"] = "center"
        GButton_434["text"] = "Button"
        GButton_434.place(x=190,y=200,width=70,height=25)
        GButton_434["command"] = self.GButton_434_command

        GButton_11=tk.Button(root)
        GButton_11["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_11["font"] = ft
        GButton_11["fg"] = "#000000"
        GButton_11["justify"] = "center"
        GButton_11["text"] = "Button"
        GButton_11.place(x=120,y=80,width=70,height=25)
        GButton_11["command"] = self.GButton_11_command

        GButton_940=tk.Button(root)
        GButton_940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#000000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Button"
        GButton_940.place(x=190,y=80,width=70,height=25)
        GButton_940["command"] = self.GButton_940_command

        GButton_338=tk.Button(root)
        GButton_338["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_338["font"] = ft
        GButton_338["fg"] = "#000000"
        GButton_338["justify"] = "center"
        GButton_338["text"] = "Button"
        GButton_338.place(x=260,y=80,width=70,height=25)
        GButton_338["command"] = self.GButton_338_command

        GLabel_140=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_140["font"] = ft
        GLabel_140["fg"] = "#333333"
        GLabel_140["justify"] = "center"
        GLabel_140["text"] = "label"
        GLabel_140.place(x=40,y=230,width=322,height=30)

        GLabel_250=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_250["font"] = ft
        GLabel_250["fg"] = "#333333"
        GLabel_250["justify"] = "center"
        GLabel_250["text"] = "label"
        GLabel_250.place(x=40,y=260,width=319,height=30)

    def GButton_537_command(self):
        print("command")


    def GButton_387_command(self):
        print("command")


    def GButton_721_command(self):
        print("command")


    def GButton_385_command(self):
        print("command")


    def GButton_329_command(self):
        print("command")


    def GButton_18_command(self):
        print("command")


    def GButton_522_command(self):
        print("command")


    def GButton_826_command(self):
        print("command")


    def GButton_737_command(self):
        print("command")


    def GButton_98_command(self):
        print("command")


    def GButton_321_command(self):
        print("command")


    def GButton_164_command(self):
        print("command")


    def GButton_459_command(self):
        print("command")


    def GButton_882_command(self):
        print("command")


    def GButton_817_command(self):
        print("command")


    def GButton_74_command(self):
        print("command")


    def GButton_75_command(self):
        print("command")


    def GButton_515_command(self):
        print("command")


    def GButton_834_command(self):
        print("command")


    def GButton_475_command(self):
        print("command")


    def GButton_900_command(self):
        print("command")


    def GButton_619_command(self):
        print("command")


    def GButton_418_command(self):
        print("command")


    def GButton_595_command(self):
        print("command")


    def GButton_434_command(self):
        print("command")


    def GButton_11_command(self):
        print("command")


    def GButton_940_command(self):
        print("command")


    def GButton_338_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
