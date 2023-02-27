import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=491
        height=286
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_439=tk.Entry(root)
        GLineEdit_439["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_439["font"] = ft
        GLineEdit_439["fg"] = "#333333"
        GLineEdit_439["justify"] = "center"
        GLineEdit_439["text"] = "Entry"
        GLineEdit_439.place(x=100,y=90,width=109,height=30)

        GLineEdit_750=tk.Entry(root)
        GLineEdit_750["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_750["font"] = ft
        GLineEdit_750["fg"] = "#333333"
        GLineEdit_750["justify"] = "center"
        GLineEdit_750["text"] = "Entry"
        GLineEdit_750.place(x=100,y=160,width=108,height=30)

        GButton_550=tk.Button(root)
        GButton_550["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_550["font"] = ft
        GButton_550["fg"] = "#000000"
        GButton_550["justify"] = "center"
        GButton_550["text"] = "Button"
        GButton_550.place(x=120,y=220,width=70,height=25)
        GButton_550["command"] = self.GButton_550_command

        GButton_967=tk.Button(root)
        GButton_967["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_967["font"] = ft
        GButton_967["fg"] = "#000000"
        GButton_967["justify"] = "center"
        GButton_967["text"] = "Button"
        GButton_967.place(x=210,y=220,width=70,height=25)
        GButton_967["command"] = self.GButton_967_command

        GListBox_767=tk.Listbox(root)
        GListBox_767["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_767["font"] = ft
        GListBox_767["fg"] = "#333333"
        GListBox_767["justify"] = "center"
        GListBox_767.place(x=290,y=40,width=133,height=220)

        GLabel_318=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_318["font"] = ft
        GLabel_318["fg"] = "#333333"
        GLabel_318["justify"] = "center"
        GLabel_318["text"] = "label"
        GLabel_318.place(x=120,y=50,width=70,height=25)

        GLabel_927=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_927["font"] = ft
        GLabel_927["fg"] = "#333333"
        GLabel_927["justify"] = "center"
        GLabel_927["text"] = "label"
        GLabel_927.place(x=120,y=130,width=70,height=25)

        GLabel_864=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_864["font"] = ft
        GLabel_864["fg"] = "#333333"
        GLabel_864["justify"] = "center"
        GLabel_864["text"] = "label"
        GLabel_864.place(x=320,y=0,width=70,height=25)

    def GButton_550_command(self):
        print("command")


    def GButton_967_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
