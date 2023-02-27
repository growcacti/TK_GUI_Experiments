import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=163
        height=825
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
        GButton_537.place(x=0,y=30,width=70,height=25)
        GButton_537["command"] = self.GButton_537_command

        GButton_387=tk.Button(root)
        GButton_387["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_387["font"] = ft
        GButton_387["fg"] = "#000000"
        GButton_387["justify"] = "center"
        GButton_387["text"] = "Button"
        GButton_387.place(x=80,y=30,width=70,height=25)
        GButton_387["command"] = self.GButton_387_command

        GButton_721=tk.Button(root)
        GButton_721["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_721["font"] = ft
        GButton_721["fg"] = "#000000"
        GButton_721["justify"] = "center"
        GButton_721["text"] = "Button"
        GButton_721.place(x=0,y=240,width=70,height=25)
        GButton_721["command"] = self.GButton_721_command

        GButton_385=tk.Button(root)
        GButton_385["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_385["font"] = ft
        GButton_385["fg"] = "#000000"
        GButton_385["justify"] = "center"
        GButton_385["text"] = "Button"
        GButton_385.place(x=80,y=450,width=70,height=25)
        GButton_385["command"] = self.GButton_385_command

        GButton_329=tk.Button(root)
        GButton_329["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_329["font"] = ft
        GButton_329["fg"] = "#000000"
        GButton_329["justify"] = "center"
        GButton_329["text"] = "Button"
        GButton_329.place(x=0,y=60,width=70,height=25)
        GButton_329["command"] = self.GButton_329_command

        GButton_18=tk.Button(root)
        GButton_18["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_18["font"] = ft
        GButton_18["fg"] = "#000000"
        GButton_18["justify"] = "center"
        GButton_18["text"] = "Button"
        GButton_18.place(x=80,y=60,width=70,height=25)
        GButton_18["command"] = self.GButton_18_command

        GButton_522=tk.Button(root)
        GButton_522["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_522["font"] = ft
        GButton_522["fg"] = "#000000"
        GButton_522["justify"] = "center"
        GButton_522["text"] = "Button"
        GButton_522.place(x=80,y=270,width=70,height=25)
        GButton_522["command"] = self.GButton_522_command

        GButton_826=tk.Button(root)
        GButton_826["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_826["font"] = ft
        GButton_826["fg"] = "#000000"
        GButton_826["justify"] = "center"
        GButton_826["text"] = "Button"
        GButton_826.place(x=0,y=420,width=70,height=25)
        GButton_826["command"] = self.GButton_826_command

        GButton_737=tk.Button(root)
        GButton_737["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_737["font"] = ft
        GButton_737["fg"] = "#000000"
        GButton_737["justify"] = "center"
        GButton_737["text"] = "Button"
        GButton_737.place(x=0,y=120,width=70,height=25)
        GButton_737["command"] = self.GButton_737_command

        GButton_98=tk.Button(root)
        GButton_98["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_98["font"] = ft
        GButton_98["fg"] = "#000000"
        GButton_98["justify"] = "center"
        GButton_98["text"] = "Button"
        GButton_98.place(x=80,y=150,width=70,height=25)
        GButton_98["command"] = self.GButton_98_command

        GButton_321=tk.Button(root)
        GButton_321["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_321["font"] = ft
        GButton_321["fg"] = "#000000"
        GButton_321["justify"] = "center"
        GButton_321["text"] = "Button"
        GButton_321.place(x=0,y=330,width=70,height=25)
        GButton_321["command"] = self.GButton_321_command

        GButton_164=tk.Button(root)
        GButton_164["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_164["font"] = ft
        GButton_164["fg"] = "#000000"
        GButton_164["justify"] = "center"
        GButton_164["text"] = "Button"
        GButton_164.place(x=80,y=420,width=70,height=25)
        GButton_164["command"] = self.GButton_164_command

        GButton_459=tk.Button(root)
        GButton_459["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_459["font"] = ft
        GButton_459["fg"] = "#000000"
        GButton_459["justify"] = "center"
        GButton_459["text"] = "Button"
        GButton_459.place(x=0,y=150,width=70,height=25)
        GButton_459["command"] = self.GButton_459_command

        GButton_817=tk.Button(root)
        GButton_817["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_817["font"] = ft
        GButton_817["fg"] = "#000000"
        GButton_817["justify"] = "center"
        GButton_817["text"] = "Button"
        GButton_817.place(x=0,y=90,width=70,height=25)
        GButton_817["command"] = self.GButton_817_command

        GButton_74=tk.Button(root)
        GButton_74["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_74["font"] = ft
        GButton_74["fg"] = "#000000"
        GButton_74["justify"] = "center"
        GButton_74["text"] = "Button"
        GButton_74.place(x=80,y=210,width=70,height=25)
        GButton_74["command"] = self.GButton_74_command

        GButton_75=tk.Button(root)
        GButton_75["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_75["font"] = ft
        GButton_75["fg"] = "#000000"
        GButton_75["justify"] = "center"
        GButton_75["text"] = "Button"
        GButton_75.place(x=80,y=180,width=70,height=25)
        GButton_75["command"] = self.GButton_75_command

        GButton_515=tk.Button(root)
        GButton_515["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_515["font"] = ft
        GButton_515["fg"] = "#000000"
        GButton_515["justify"] = "center"
        GButton_515["text"] = "Button"
        GButton_515.place(x=80,y=300,width=70,height=25)
        GButton_515["command"] = self.GButton_515_command

        GButton_834=tk.Button(root)
        GButton_834["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_834["font"] = ft
        GButton_834["fg"] = "#000000"
        GButton_834["justify"] = "center"
        GButton_834["text"] = "Button"
        GButton_834.place(x=80,y=330,width=70,height=25)
        GButton_834["command"] = self.GButton_834_command

        GButton_475=tk.Button(root)
        GButton_475["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_475["font"] = ft
        GButton_475["fg"] = "#000000"
        GButton_475["justify"] = "center"
        GButton_475["text"] = "Button"
        GButton_475.place(x=0,y=360,width=70,height=25)
        GButton_475["command"] = self.GButton_475_command

        GButton_900=tk.Button(root)
        GButton_900["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_900["font"] = ft
        GButton_900["fg"] = "#000000"
        GButton_900["justify"] = "center"
        GButton_900["text"] = "Button"
        GButton_900.place(x=80,y=390,width=70,height=25)
        GButton_900["command"] = self.GButton_900_command

        GButton_619=tk.Button(root)
        GButton_619["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_619["font"] = ft
        GButton_619["fg"] = "#000000"
        GButton_619["justify"] = "center"
        GButton_619["text"] = "Button"
        GButton_619.place(x=0,y=210,width=70,height=25)
        GButton_619["command"] = self.GButton_619_command

        GButton_418=tk.Button(root)
        GButton_418["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_418["font"] = ft
        GButton_418["fg"] = "#000000"
        GButton_418["justify"] = "center"
        GButton_418["text"] = "Button"
        GButton_418.place(x=80,y=240,width=70,height=25)
        GButton_418["command"] = self.GButton_418_command

        GButton_595=tk.Button(root)
        GButton_595["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_595["font"] = ft
        GButton_595["fg"] = "#000000"
        GButton_595["justify"] = "center"
        GButton_595["text"] = "Button"
        GButton_595.place(x=0,y=300,width=70,height=25)
        GButton_595["command"] = self.GButton_595_command

        GButton_434=tk.Button(root)
        GButton_434["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_434["font"] = ft
        GButton_434["fg"] = "#000000"
        GButton_434["justify"] = "center"
        GButton_434["text"] = "Button"
        GButton_434.place(x=0,y=270,width=70,height=25)
        GButton_434["command"] = self.GButton_434_command

        GButton_11=tk.Button(root)
        GButton_11["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_11["font"] = ft
        GButton_11["fg"] = "#000000"
        GButton_11["justify"] = "center"
        GButton_11["text"] = "Button"
        GButton_11.place(x=80,y=90,width=70,height=25)
        GButton_11["command"] = self.GButton_11_command

        GButton_940=tk.Button(root)
        GButton_940["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_940["font"] = ft
        GButton_940["fg"] = "#000000"
        GButton_940["justify"] = "center"
        GButton_940["text"] = "Button"
        GButton_940.place(x=80,y=360,width=70,height=25)
        GButton_940["command"] = self.GButton_940_command

        GButton_338=tk.Button(root)
        GButton_338["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_338["font"] = ft
        GButton_338["fg"] = "#000000"
        GButton_338["justify"] = "center"
        GButton_338["text"] = "Button"
        GButton_338.place(x=0,y=390,width=70,height=25)
        GButton_338["command"] = self.GButton_338_command

        GButton_396=tk.Button(root)
        GButton_396["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_396["font"] = ft
        GButton_396["fg"] = "#000000"
        GButton_396["justify"] = "center"
        GButton_396["text"] = "Button"
        GButton_396.place(x=0,y=450,width=70,height=25)
        GButton_396["command"] = self.GButton_396_command

        GButton_530=tk.Button(root)
        GButton_530["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_530["font"] = ft
        GButton_530["fg"] = "#000000"
        GButton_530["justify"] = "center"
        GButton_530["text"] = "Button"
        GButton_530.place(x=80,y=480,width=70,height=25)
        GButton_530["command"] = self.GButton_530_command

        GButton_139=tk.Button(root)
        GButton_139["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_139["font"] = ft
        GButton_139["fg"] = "#000000"
        GButton_139["justify"] = "center"
        GButton_139["text"] = "Button"
        GButton_139.place(x=0,y=480,width=70,height=25)
        GButton_139["command"] = self.GButton_139_command

        GButton_91=tk.Button(root)
        GButton_91["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_91["font"] = ft
        GButton_91["fg"] = "#000000"
        GButton_91["justify"] = "center"
        GButton_91["text"] = "Button"
        GButton_91.place(x=0,y=570,width=70,height=25)
        GButton_91["command"] = self.GButton_91_command

        GButton_291=tk.Button(root)
        GButton_291["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_291["font"] = ft
        GButton_291["fg"] = "#000000"
        GButton_291["justify"] = "center"
        GButton_291["text"] = "Button"
        GButton_291.place(x=80,y=120,width=70,height=25)
        GButton_291["command"] = self.GButton_291_command

        GButton_613=tk.Button(root)
        GButton_613["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_613["font"] = ft
        GButton_613["fg"] = "#000000"
        GButton_613["justify"] = "center"
        GButton_613["text"] = "Button"
        GButton_613.place(x=0,y=180,width=70,height=25)
        GButton_613["command"] = self.GButton_613_command

        GButton_412=tk.Button(root)
        GButton_412["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_412["font"] = ft
        GButton_412["fg"] = "#000000"
        GButton_412["justify"] = "center"
        GButton_412["text"] = "Button"
        GButton_412.place(x=80,y=0,width=70,height=25)
        GButton_412["command"] = self.GButton_412_command

        GButton_652=tk.Button(root)
        GButton_652["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_652["font"] = ft
        GButton_652["fg"] = "#000000"
        GButton_652["justify"] = "center"
        GButton_652["text"] = "Button"
        GButton_652.place(x=0,y=510,width=70,height=25)
        GButton_652["command"] = self.GButton_652_command

        GButton_66=tk.Button(root)
        GButton_66["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_66["font"] = ft
        GButton_66["fg"] = "#000000"
        GButton_66["justify"] = "center"
        GButton_66["text"] = "Button"
        GButton_66.place(x=80,y=510,width=70,height=25)
        GButton_66["command"] = self.GButton_66_command

        GButton_810=tk.Button(root)
        GButton_810["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_810["font"] = ft
        GButton_810["fg"] = "#000000"
        GButton_810["justify"] = "center"
        GButton_810["text"] = "Button"
        GButton_810.place(x=0,y=540,width=70,height=25)
        GButton_810["command"] = self.GButton_810_command

        GButton_682=tk.Button(root)
        GButton_682["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_682["font"] = ft
        GButton_682["fg"] = "#000000"
        GButton_682["justify"] = "center"
        GButton_682["text"] = "Button"
        GButton_682.place(x=80,y=540,width=70,height=25)
        GButton_682["command"] = self.GButton_682_command

        GButton_91=tk.Button(root)
        GButton_91["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_91["font"] = ft
        GButton_91["fg"] = "#000000"
        GButton_91["justify"] = "center"
        GButton_91["text"] = "Button"
        GButton_91.place(x=0,y=570,width=70,height=25)
        GButton_91["command"] = self.GButton_91_command

        GButton_994=tk.Button(root)
        GButton_994["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_994["font"] = ft
        GButton_994["fg"] = "#000000"
        GButton_994["justify"] = "center"
        GButton_994["text"] = "Button"
        GButton_994.place(x=80,y=570,width=70,height=25)
        GButton_994["command"] = self.GButton_994_command

        GButton_322=tk.Button(root)
        GButton_322["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_322["font"] = ft
        GButton_322["fg"] = "#000000"
        GButton_322["justify"] = "center"
        GButton_322["text"] = "Button"
        GButton_322.place(x=0,y=600,width=70,height=25)
        GButton_322["command"] = self.GButton_322_command

        GButton_659=tk.Button(root)
        GButton_659["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_659["font"] = ft
        GButton_659["fg"] = "#000000"
        GButton_659["justify"] = "center"
        GButton_659["text"] = "Button"
        GButton_659.place(x=80,y=600,width=70,height=25)
        GButton_659["command"] = self.GButton_659_command

        GButton_547=tk.Button(root)
        GButton_547["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_547["font"] = ft
        GButton_547["fg"] = "#000000"
        GButton_547["justify"] = "center"
        GButton_547["text"] = "Button"
        GButton_547.place(x=0,y=630,width=70,height=25)
        GButton_547["command"] = self.GButton_547_command

        GButton_795=tk.Button(root)
        GButton_795["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_795["font"] = ft
        GButton_795["fg"] = "#000000"
        GButton_795["justify"] = "center"
        GButton_795["text"] = "Button"
        GButton_795.place(x=80,y=630,width=70,height=25)
        GButton_795["command"] = self.GButton_795_command

        GButton_228=tk.Button(root)
        GButton_228["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_228["font"] = ft
        GButton_228["fg"] = "#000000"
        GButton_228["justify"] = "center"
        GButton_228["text"] = "Button"
        GButton_228.place(x=0,y=660,width=70,height=25)
        GButton_228["command"] = self.GButton_228_command

        GButton_131=tk.Button(root)
        GButton_131["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_131["font"] = ft
        GButton_131["fg"] = "#000000"
        GButton_131["justify"] = "center"
        GButton_131["text"] = "Button"
        GButton_131.place(x=80,y=660,width=70,height=25)
        GButton_131["command"] = self.GButton_131_command

        GButton_804=tk.Button(root)
        GButton_804["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_804["font"] = ft
        GButton_804["fg"] = "#000000"
        GButton_804["justify"] = "center"
        GButton_804["text"] = "Button"
        GButton_804.place(x=0,y=690,width=70,height=25)
        GButton_804["command"] = self.GButton_804_command

        GButton_579=tk.Button(root)
        GButton_579["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_579["font"] = ft
        GButton_579["fg"] = "#000000"
        GButton_579["justify"] = "center"
        GButton_579["text"] = "Button"
        GButton_579.place(x=80,y=690,width=70,height=25)
        GButton_579["command"] = self.GButton_579_command

        GButton_524=tk.Button(root)
        GButton_524["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_524["font"] = ft
        GButton_524["fg"] = "#000000"
        GButton_524["justify"] = "center"
        GButton_524["text"] = "Button"
        GButton_524.place(x=0,y=720,width=70,height=25)
        GButton_524["command"] = self.GButton_524_command

        GButton_187=tk.Button(root)
        GButton_187["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_187["font"] = ft
        GButton_187["fg"] = "#000000"
        GButton_187["justify"] = "center"
        GButton_187["text"] = "Button"
        GButton_187.place(x=80,y=720,width=70,height=25)
        GButton_187["command"] = self.GButton_187_command

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


    def GButton_396_command(self):
        print("command")


    def GButton_530_command(self):
        print("command")


    def GButton_139_command(self):
        print("command")


    def GButton_91_command(self):
        print("command")


    def GButton_291_command(self):
        print("command")


    def GButton_613_command(self):
        print("command")


    def GButton_412_command(self):
        print("command")


    def GButton_652_command(self):
        print("command")


    def GButton_66_command(self):
        print("command")


    def GButton_810_command(self):
        print("command")


    def GButton_682_command(self):
        print("command")


    def GButton_91_command(self):
        print("command")


    def GButton_994_command(self):
        print("command")


    def GButton_322_command(self):
        print("command")


    def GButton_659_command(self):
        print("command")


    def GButton_547_command(self):
        print("command")


    def GButton_795_command(self):
        print("command")


    def GButton_228_command(self):
        print("command")


    def GButton_131_command(self):
        print("command")


    def GButton_804_command(self):
        print("command")


    def GButton_579_command(self):
        print("command")


    def GButton_524_command(self):
        print("command")


    def GButton_187_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
