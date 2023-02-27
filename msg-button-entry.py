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

        taq481=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        taq481["font"] = ft
        taq481["fg"] = "#333333"
        taq481["justify"] = "center"
        taq481["text"] = "label"
        taq481.place(x=230,y=150,width=70,height=25)

        b905=tk.Button(root)
        b905["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b905["font"] = ft
        b905["fg"] = "#000000"
        b905["justify"] = "center"
        b905["text"] = "Button"
        b905.place(x=80,y=260,width=70,height=25)
        b905["command"] = self.b905_command

        b785=tk.Button(root)
        b785["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b785["font"] = ft
        b785["fg"] = "#000000"
        b785["justify"] = "center"
        b785["text"] = "Button"
        b785.place(x=240,y=260,width=70,height=25)
        b785["command"] = self.b785_command

        b648=tk.Button(root)
        b648["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        b648["font"] = ft
        b648["fg"] = "#000000"
        b648["justify"] = "center"
        b648["text"] = "Button"
        b648.place(x=360,y=260,width=70,height=25)
        b648["command"] = self.b648_command

        m_40=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        m_40["font"] = ft
        m_40["fg"] = "#333333"
        m_40["justify"] = "center"
        m_40["text"] = "Message"
        m_40.place(x=80,y=360,width=389,height=80)

    def b905_command(self):
        print("command")


    def b785_command(self):
        print("command")


    def b648_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
