import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=397
        height=369
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_213=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_213["font"] = ft
        GMessage_213["fg"] = "#333333"
        GMessage_213["justify"] = "center"
        GMessage_213["text"] = "Message"
        GMessage_213.place(x=190,y=10,width=147,height=51)

        GMessage_732=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_732["font"] = ft
        GMessage_732["fg"] = "#333333"
        GMessage_732["justify"] = "center"
        GMessage_732["text"] = "Message"
        GMessage_732.place(x=170,y=100,width=198,height=55)

        GMessage_733=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_733["font"] = ft
        GMessage_733["fg"] = "#333333"
        GMessage_733["justify"] = "center"
        GMessage_733["text"] = "Message"
        GMessage_733.place(x=200,y=210,width=144,height=46)

        GMessage_731=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_731["font"] = ft
        GMessage_731["fg"] = "#333333"
        GMessage_731["justify"] = "center"
        GMessage_731["text"] = "Message"
        GMessage_731.place(x=200,y=280,width=144,height=77)

        GLineEdit_349=tk.Entry(root)
        GLineEdit_349["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_349["font"] = ft
        GLineEdit_349["fg"] = "#333333"
        GLineEdit_349["justify"] = "center"
        GLineEdit_349["text"] = "Entry"
        GLineEdit_349.place(x=40,y=30,width=152,height=30)

        GLineEdit_453=tk.Entry(root)
        GLineEdit_453["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_453["font"] = ft
        GLineEdit_453["fg"] = "#333333"
        GLineEdit_453["justify"] = "center"
        GLineEdit_453["text"] = "Entry"
        GLineEdit_453.place(x=50,y=110,width=143,height=32)

        GLineEdit_726=tk.Entry(root)
        GLineEdit_726["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_726["font"] = ft
        GLineEdit_726["fg"] = "#333333"
        GLineEdit_726["justify"] = "center"
        GLineEdit_726["text"] = "Entry"
        GLineEdit_726.place(x=50,y=190,width=145,height=30)

        GLineEdit_973=tk.Entry(root)
        GLineEdit_973["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_973["font"] = ft
        GLineEdit_973["fg"] = "#333333"
        GLineEdit_973["justify"] = "center"
        GLineEdit_973["text"] = "Entry"
        GLineEdit_973.place(x=50,y=260,width=146,height=34)

        GButton_949=tk.Button(root)
        GButton_949["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_949["font"] = ft
        GButton_949["fg"] = "#000000"
        GButton_949["justify"] = "center"
        GButton_949["text"] = "Button"
        GButton_949.place(x=80,y=70,width=70,height=25)
        GButton_949["command"] = self.GButton_949_command

        GButton_214=tk.Button(root)
        GButton_214["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_214["font"] = ft
        GButton_214["fg"] = "#000000"
        GButton_214["justify"] = "center"
        GButton_214["text"] = "Button"
        GButton_214.place(x=80,y=150,width=70,height=25)
        GButton_214["command"] = self.GButton_214_command

        GButton_773=tk.Button(root)
        GButton_773["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_773["font"] = ft
        GButton_773["fg"] = "#000000"
        GButton_773["justify"] = "center"
        GButton_773["text"] = "Button"
        GButton_773.place(x=90,y=230,width=70,height=25)
        GButton_773["command"] = self.GButton_773_command

        GButton_349=tk.Button(root)
        GButton_349["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_349["font"] = ft
        GButton_349["fg"] = "#000000"
        GButton_349["justify"] = "center"
        GButton_349["text"] = "Button"
        GButton_349.place(x=90,y=310,width=70,height=25)
        GButton_349["command"] = self.GButton_349_command

    def GButton_949_command(self):
        print("command")


    def GButton_214_command(self):
        print("command")


    def GButton_773_command(self):
        print("command")


    def GButton_349_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
