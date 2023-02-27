import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("GUI")
        #setting window size
        width=1252
        height=898
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_765=tk.Entry(root)
        GLineEdit_765["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_765["font"] = ft
        GLineEdit_765["fg"] = "#333333"
        GLineEdit_765["justify"] = "center"
        GLineEdit_765["text"] = "Entry"
        GLineEdit_765.place(x=170,y=140,width=1058,height=585)

        GLineEdit_109=tk.Entry(root)
        GLineEdit_109["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_109["font"] = ft
        GLineEdit_109["fg"] = "#333333"
        GLineEdit_109["justify"] = "center"
        GLineEdit_109["text"] = "Entry"
        GLineEdit_109.place(x=160,y=20,width=1069,height=87)

        lbox_34=tk.Listbox(root)
        lbox_34["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox_34["font"] = ft
        lbox_34["fg"] = "#333333"
        lbox_34["justify"] = "center"
        lbox_34.place(x=120,y=140,width=31,height=686)

        b_439=tk.Button(root)
        b_439["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_439["font"] = ft
        b_439["fg"] = "#273134"
        b_439["justify"] = "center"
        b_439["text"] = "Button"
        b_439.place(x=20,y=70,width=70,height=25)
        b_439["command"] = self.b_439_command

        b_749=tk.Button(root)
        b_749["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_749["font"] = ft
        b_749["fg"] = "#273134"
        b_749["justify"] = "center"
        b_749["text"] = "Button"
        b_749.place(x=20,y=100,width=70,height=25)
        b_749["command"] = self.b_749_command

        b_670=tk.Button(root)
        b_670["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_670["font"] = ft
        b_670["fg"] = "#273134"
        b_670["justify"] = "center"
        b_670["text"] = "Button"
        b_670.place(x=20,y=130,width=70,height=25)
        b_670["command"] = self.b_670_command

        b_975=tk.Button(root)
        b_975["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_975["font"] = ft
        b_975["fg"] = "#273134"
        b_975["justify"] = "center"
        b_975["text"] = "Button"
        b_975.place(x=20,y=160,width=70,height=25)
        b_975["command"] = self.b_975_command

        b_767=tk.Button(root)
        b_767["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_767["font"] = ft
        b_767["fg"] = "#273134"
        b_767["justify"] = "center"
        b_767["text"] = "Button"
        b_767.place(x=20,y=190,width=70,height=25)
        b_767["command"] = self.b_767_command

        b_287=tk.Button(root)
        b_287["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_287["font"] = ft
        b_287["fg"] = "#273134"
        b_287["justify"] = "center"
        b_287["text"] = "Button"
        b_287.place(x=20,y=220,width=70,height=25)
        b_287["command"] = self.b_287_command

        b_47=tk.Button(root)
        b_47["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_47["font"] = ft
        b_47["fg"] = "#273134"
        b_47["justify"] = "center"
        b_47["text"] = "Button"
        b_47.place(x=20,y=580,width=70,height=25)
        b_47["command"] = self.b_47_command

        b_489=tk.Button(root)
        b_489["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_489["font"] = ft
        b_489["fg"] = "#273134"
        b_489["justify"] = "center"
        b_489["text"] = "Button"
        b_489.place(x=20,y=280,width=70,height=25)
        b_489["command"] = self.b_489_command

        b_145=tk.Button(root)
        b_145["bg"] = "#f7f7f7"b_234_c
        ft = tkFont.Font(family='Times',size=10)
        b_145["font"] = ft
        b_145["fg"] = "#273134"
        b_145["justify"] = "center"
        b_145["text"] = "Button"
        b_145.place(x=20,y=310,width=70,height=25)
        b_145["command"] = self.b_145_command

        b_479=tk.Button(root)
        b_479["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_479["font"] = ft
        b_479["fg"] = "#273134"
        b_479["justify"] = "center"
        b_479["text"] = "Button"
        b_479.place(x=20,y=340,width=70,height=25)
        b_479["command"] = self.b_479_command

        b_955=tk.Button(root)
        b_955["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_955["font"] = ft
        b_955["fg"] = "#273134"
        b_955["justify"] = "center"
        b_955["text"] = "Button"
        b_955.place(x=20,y=370,width=70,height=25)
        b_955["command"] = self.b_955_command

        b_124=tk.Button(root)
        b_124["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_124["font"] = ft
        b_124["fg"] = "#273134"
        b_124["justify"] = "center"
        b_124["text"] = "Button"
        b_124.place(x=20,y=430,width=70,height=25)
        b_124["command"] = self.b_124_command

        b_996=tk.Button(root)
        b_996["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_996["font"] = ft
        b_996["fg"] = "#273134"
        b_996["justify"] = "center"
        b_996["text"] = "Button"
        b_996.place(x=20,y=520,width=70,height=25)
        b_996["command"] = self.b_996_command

        b_364=tk.Button(root)
        b_364["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_364["font"] = ft
        b_364["fg"] = "#273134"
        b_364["justify"] = "center"
        b_364["text"] = "Button"
        b_364.place(x=20,y=490,width=70,height=25)
        b_364["command"] = self.b_364_command

        b_404=tk.Button(root)
        b_404["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_404["font"] = ft
        b_404["fg"] = "#273134"
        b_404["justify"] = "center"
        b_404["text"] = "Button"
        b_404.place(x=20,y=460,width=70,height=25)
        b_404["command"] = self.b_404_command

        b_773=tk.Button(root)
        b_773["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_773["font"] = ft
        b_773["fg"] = "#273134"
        b_773["justify"] = "center"
        b_773["text"] = "Button"
        b_773.place(x=20,y=400,width=70,height=25)
        b_773["command"] = self.b_773_command

        b_422=tk.Button(root)
        b_422["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_422["font"] = ft
        b_422["fg"] = "#273134"
        b_422["justify"] = "center"
        b_422["text"] = "Button"
        b_422.place(x=20,y=550,width=70,height=25)
        b_422["command"] = self.b_422_command

        b_47=tk.Button(root)
        b_47["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_47["font"] = ft
        b_47["fg"] = "#273134"
        b_47["justify"] = "center"
        b_47["text"] = "Button"
        b_47.place(x=20,y=580,width=70,height=25)
        b_47["command"] = self.b_47_command

        b_447=tk.Button(root)
        b_447["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_447["font"] = ft
        b_447["fg"] = "#273134"
        b_447["justify"] = "center"
        b_447["text"] = "Button"b_234_c
        b_447.place(x=20,y=670,width=70,height=25)
        b_447["command"] = self.b_447_command

        b_760=tk.Button(root)
        b_760["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_760["font"] = ft
        b_760["fg"] = "#273134"
        b_760["justify"] = "center"
        b_760["text"] = "Button"
        b_760.place(x=20,y=640,width=70,height=25)
        b_760["command"] = self.b_760_command

        b_257=tk.Button(root)
        b_257["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_257["font"] = ft
        b_257["fg"] = "#273134"
        b_257["justify"] = "center"
        b_257["text"] = "Button"
        b_257.place(x=20,y=610,width=70,height=25)
        b_257["command"] = self.b_257_command

        b_482=tk.Button(root)
        b_482["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_482["font"] = ft
        b_482["fg"] = "#273134"
        b_482["justify"] = "center"
        b_482["text"] = "Button"
        b_482.place(x=20,y=250,width=70,height=25)
        b_482["command"] = self.b_482_command

        b_347=tk.Button(root)
        b_347["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_347["font"] = ft
        b_347["fg"] = "#273134"
        b_347["justify"] = "center"
        b_347["text"] = "Button"
        b_347.place(x=20,y=790,width=70,height=25)
        b_347["command"] = self.b_347_command

        b_795=tk.Button(root)
        b_795["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_795["font"] = ft
        b_795["fg"] = "#273134"
        b_795["justify"] = "center"
        b_795["text"] = "Button"
        b_795.place(x=20,y=760,width=70,height=25)
        b_795["command"] = self.b_795_command

        b_644=tk.Button(root)
        b_644["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_644["font"] = ft
        b_644["fg"] = "#273134"
        b_644["justify"] = "center"
        b_644["text"] = "Button"
        b_644.place(x=20,y=730,width=70,height=25)
        b_644["command"] = self.b_644_command

        b_420=tk.Button(root)
        b_420["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_420["font"] = ft
        b_420["fg"] = "#273134"
        b_420["justify"] = "center"
        b_420["text"] = "Button"
        b_420.place(x=20,y=700,width=70,height=25)
        b_420["command"] = self.b_420_command

        GCheckBox_904=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GCheckBox_904["font"] = ft
        GCheckBox_904["fg"] = "#333333"
        GCheckBox_904["justify"] = "center"
        GCheckBox_904["text"] = "CheckBox"
        GCheckBox_904.place(x=110,y=110,width=70,height=25)
        GCheckBox_904["offvalue"] = "0"
        GCheckBox_904["onvalue"] = "1"
        GCheckBox_904["command"] = self.GCheckBox_904_command

        GMessage_946=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_946["font"] = ft
        GMessage_946["fg"] = "#333333"
        GMessage_946["justify"] = "center"
        GMessage_946["text"] = "Message"b_234_c
        GMessage_946.place(x=170,y=750,width=759,height=127)

        b_533=tk.Button(root)
        b_533["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_533["font"] = ft
        b_533["fg"] = "#273134"
        b_533["justify"] = "center"
        b_533["text"] = "Button"
        b_533.place(x=20,y=0,width=70,height=25)
        b_533["command"] = self.b_533_command

        b_807=tk.Button(root)
        b_807["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_807["font"] = ft
        b_807["fg"] = "#273134"
        b_807["justify"] = "center"
        b_807["text"] = "Button"
        b_807.place(x=200,y=110,width=70,height=25)
        b_807["command"] = self.b_807_command

        b_91=tk.Button(root)
        b_91["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_91["font"] = ft
        b_91["fg"] = "#273134"
        b_91["justify"] = "center"
        b_91["text"] = "Button"
        b_91.place(x=270,y=110,width=70,height=25)
        b_91["command"] = self.b_91_command

        b_659=tk.Button(root)
        b_659["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_659["font"] = ft
        b_659["fg"] = "#273134"
        b_659["justify"] = "center"
        b_659["text"] = "Button"
        b_659.place(x=340,y=110,width=70,height=25)
        b_659["command"] = self.b_659_command

        b_700=tk.Button(root)
        b_700["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)b_234_c
        b_700["font"] = ft
        b_700["fg"] = "#273134"
        b_700["justify"] = "center"
        b_700["text"] = "Button"
        b_700.place(x=410,y=110,width=70,height=25)
        b_700["command"] = self.b_700_command

        b_12=tk.Button(root)
        b_12["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_12["font"] = ft
        b_12["fg"] = "#273134"
        b_12["justify"] = "center"
        b_12["text"] = "Button"
        b_12.place(x=480,y=110,width=70,height=25)
        b_12["command"] = self.b_12_command

        b_959=tk.Button(root)
        b_959["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_959["font"] = ft
        b_959["fg"] = "#273134"
        b_959["justify"] = "center"
        b_959["text"] = "Button"
        b_959.place(x=550,y=110,width=70,height=25)
        b_959["command"] = self.b_959_command

        b_423=tk.Button(root)
        b_423["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_423["font"] = ft
        b_423["fg"] = "#273134"
        b_423["justify"] = "center"
        b_423["text"] = "Button"
        b_423.place(x=630,y=110,width=70,height=25)
        b_423["command"] = self.b_423_command

        b_743=tk.Button(root)
        b_743["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)b_234_c
        b_743["font"] = ft
        b_743["fg"] = "#273134"
        b_743["justify"] = "center"
        b_743["text"] = "Button"
        b_743.place(x=720,y=110,width=70,height=25)
        b_743["command"] = self.b_743_command

        b_674=tk.Button(root)
        b_674["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_674["font"] = ft
        b_674["fg"] = "#273134"
        b_674["justify"] = "center"
        b_674["text"] = "Button"
        b_674.place(x=800,y=110,width=70,height=25)
        b_674["command"] = self.b_674_command

        b_217=tk.Button(root)
        b_217["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_217["font"] = ft
        b_217["fg"] = "#273134"
        b_217["justify"] = "center"
        b_217["text"] = "Button"
        b_217.place(x=880,y=110,width=70,height=25)
        b_217["command"] = self.b_217_command

        b_643=tk.Button(root)
        b_643["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_643["font"] = ft
        b_643["fg"] = "#273134"
        b_643["justify"] = "center"
        b_643["text"] = "Button"
        b_643.place(x=960,y=110,width=70,height=25)
        b_643["command"] = self.b_643_command

        b_234=tk.Button(root)
        b_234["bg"] = "#f7f7f7"
        ft = tkFont.Font(family='Times',size=10)
        b_234["font"] = ft
        b_234["fg"] = "#273134"
        b_234["justify"] = "center"
        b_234["text"] = "Button"
        b_234.place(x=1040,y=110,width=70,height=25)
        b_234["command"] = self.b_234_command

    def b_439_command(self):
        print("command")

b_234_c
    def b_749_command(self):
        print("command")


    def b_670_command(self):
        print("command")


    def b_975_command(self):
        print("command")


    def b_767_command(self):
        print("command")


    def b_287_command(self):
        print("command")


    def b_47_command(self):
        print("command")


    def b_489_command(self):
        print("command")


    def b_145_command(self):
        print("command")


    def b_479_command(self):
        print("command")


    def b_955_command(self):
        print("command")


    def b_124_command(self):
        print("command")


    def b_996_command(self):
        print("command")


    def b_364_command(self):b_234_c
        print("command")


    def b_404_command(self):
        print("command")


    def b_773_command(self):
        print("command")


    def b_422_command(self):
        print("command")


    def b_47_command(self):
        print("command")


    def b_447_command(self):
        print("command")


    def b_760_command(self):
        print("command")


    def b_257_command(self):
        print("command")


    def b_482_command(self):
        print("command")


    def b_347_command(self):
        print("command")


    def b_795_command(self):
        print("command")


    def b_644_command(self):
        print("command")


    def b_420_command(self):
        print("command")


    def GCheckBox_904_command(self):
        print("command")


    def b_533_command(self):
        print("command")


    def b_807_command(self):
        print("command")


    def b_91_command(self):
        print("command")


    def b_659_command(self):
        print("command")


    def b_700_command(self):
        print("command")


    def b_12_command(self):
        print("command")


    def b_959_command(self):
        print("command")


    def b_423_command(self):
        print("command")


    def b_743_command(self):
        print("command")


    def b_674_command(self):
        print("command")


    def b_217_command(self):
        print("command")


    def b_643_command(self):
        print("command")


    def b_234_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
