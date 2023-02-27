import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=706
        height=492
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        lbox867=tk.Listbox(root)
        lbox867["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox867["font"] = ft
        lbox867["fg"] = "#333333"
        lbox867["justify"] = "center"
        lbox867.place(x=40,y=50,width=80,height=25)

        lbox578=tk.Listbox(root)
        lbox578["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox578["font"] = ft
        lbox578["fg"] = "#333333"
        lbox578["justify"] = "center"
        lbox578.place(x=140,y=50,width=80,height=25)

        lbox50=tk.Listbox(root)
        lbox50["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox50["font"] = ft
        lbox50["fg"] = "#333333"
        lbox50["justify"] = "center"
        lbox50.place(x=240,y=50,width=80,height=25)

        lbox483=tk.Listbox(root)
        lbox483["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox483["font"] = ft
        lbox483["fg"] = "#333333"
        lbox483["justify"] = "center"
        lbox483.place(x=330,y=50,width=80,height=25)

        lbox356=tk.Listbox(root)
        lbox356["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox356["font"] = ft
        lbox356["fg"] = "#333333"
        lbox356["justify"] = "center"
        lbox356.place(x=430,y=50,width=80,height=25)

        lbox172=tk.Listbox(root)
        lbox172["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        lbox172["font"] = ft
        lbox172["fg"] = "#333333"
        lbox172["justify"] = "center"
        lbox172.place(x=520,y=50,width=80,height=25)

        taq651=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq651["font"] = ft
        taq651["fg"] = "#333333"
        taq651["justify"] = "center"
        taq651["text"] = "label"
        taq651.place(x=30,y=20,width=70,height=25)

        taq371=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq371["font"] = ft
        taq371["fg"] = "#333333"
        taq371["justify"] = "center"
        taq371["text"] = "label"
        taq371.place(x=130,y=20,width=70,height=25)

        taq772=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq772["font"] = ft
        taq772["fg"] = "#333333"
        taq772["justify"] = "center"
        taq772["text"] = "label"
        taq772.place(x=240,y=20,width=70,height=25)

        taq626=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq626["font"] = ft
        taq626["fg"] = "#333333"
        taq626["justify"] = "center"
        taq626["text"] = "label"
        taq626.place(x=340,y=20,width=70,height=25)

        taq299=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq299["font"] = ft
        taq299["fg"] = "#333333"
        taq299["justify"] = "center"
        taq299["text"] = "label"
        taq299.place(x=420,y=20,width=70,height=25)

        taq500=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq500["font"] = ft
        taq500["fg"] = "#333333"
        taq500["justify"] = "center"
        taq500["text"] = "label"
        taq500.place(x=530,y=20,width=70,height=25)

        b308=tk.Button(root)
        b308["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b308["font"] = ft
        b308["fg"] = "#000000"
        b308["justify"] = "center"
        b308["text"] = "Button"
        b308.place(x=50,y=450,width=70,height=25)
        b308["command"] = self.b308_command

        b723=tk.Button(root)
        b723["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b723["font"] = ft
        b723["fg"] = "#000000"
        b723["justify"] = "center"
        b723["text"] = "Button"
        b723.place(x=150,y=450,width=70,height=25)
        b723["command"] = self.b723_command

        b443=tk.Button(root)
        b443["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b443["font"] = ft
        b443["fg"] = "#000000"
        b443["justify"] = "center"
        b443["text"] = "Button"
        b443.place(x=250,y=450,width=70,height=25)
        b443["command"] = self.b443_command

        b507=tk.Button(root)
        b507["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b507["font"] = ft
        b507["fg"] = "#000000"
        b507["justify"] = "center"
        b507["text"] = "Button"
        b507.place(x=360,y=450,width=70,height=25)
        b507["command"] = self.b507_command

        b210=tk.Button(root)
        b210["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b210["font"] = ft
        b210["fg"] = "#000000"
        b210["justify"] = "center"
        b210["text"] = "Button"
        b210.place(x=450,y=450,width=70,height=25)
        b210["command"] = self.b210_command

        b691=tk.Button(root)
        b691["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b691["font"] = ft
        b691["fg"] = "#000000"
        b691["justify"] = "center"
        b691["text"] = "Button"
        b691.place(x=540,y=450,width=70,height=25)
        b691["command"] = self.b691_command

    def b308_command(self):
        print("command")


    def b723_command(self):
        print("command")


    def b443_command(self):
        print("command")


    def b507_command(self):
        print("command")


    def b210_command(self):
        print("command")


    def b691_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
