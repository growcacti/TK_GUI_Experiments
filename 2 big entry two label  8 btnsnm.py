import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 1331
        height = 792
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        _308 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        _308["font"] = ft
        _308["fg"] = "#333333"
        _308["justify"] = "center"
        _308["text"] = "label"
        _308.place(x=210, y=50, width=70, height=25)

        GLineEdit_12 = tk.Text(root)
        GLineEdit_12.place(x=0, y=180, width=490, height=329)

        _310 = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        _310["font"] = ft
        _310["fg"] = "#333333"
        _310["justify"] = "center"
        _310["text"] = "label"
        _310.place(x=1040, y=50, width=70, height=25)

        GLineEdit_941 = tk.Text(root)
        GLineEdit_941.place(x=830, y=160, width=458, height=354)

        b52 = tk.Button(root)
        b52["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b52["font"] = ft
        b52["fg"] = "#000000"
        b52["justify"] = "center"
        b52["text"] = "Button"
        b52.place(x=60, y=570, width=70, height=25)
        b52["command"] = self.b52_command

        b669 = tk.Button(root)
        b669["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b669["font"] = ft
        b669["fg"] = "#000000"
        b669["justify"] = "center"
        b669["text"] = "Button"
        b669.place(x=150, y=570, width=70, height=25)
        b669["command"] = self.b669_command

        b644 = tk.Button(root)
        b644["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b644["font"] = ft
        b644["fg"] = "#000000"
        b644["justify"] = "center"
        b644["text"] = "Button"
        b644.place(x=240, y=570, width=70, height=25)
        b644["command"] = self.b644_command

        b278 = tk.Button(root)
        b278["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b278["font"] = ft
        b278["fg"] = "#000000"
        b278["justify"] = "center"
        b278["text"] = "Button"
        b278.place(x=330, y=570, width=70, height=25)
        b278["command"] = self.b278_command

        b221 = tk.Button(root)
        b221["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b221["font"] = ft
        b221["fg"] = "#000000"
        b221["justify"] = "center"
        b221["text"] = "Button"
        b221.place(x=890, y=570, width=70, height=25)
        b221["command"] = self.b221_command

        b859 = tk.Button(root)
        b859["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b859["font"] = ft
        b859["fg"] = "#000000"
        b859["justify"] = "center"
        b859["text"] = "Button"
        b859.place(x=980, y=570, width=70, height=25)
        b859["command"] = self.b859_command

        b397 = tk.Button(root)
        b397["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b397["font"] = ft
        b397["fg"] = "#000000"
        b397["justify"] = "center"
        b397["text"] = "Button"
        b397.place(x=1070, y=570, width=70, height=25)
        b397["command"] = self.b397_command

        b340 = tk.Button(root)
        b340["bg"] = "#efefef"
        ft = tkFont.Font(family="Times", size=10)
        b340["font"] = ft
        b340["fg"] = "#000000"
        b340["justify"] = "center"
        b340["text"] = "Button"
        b340.place(x=1160, y=570, width=70, height=25)
        b340["command"] = self.b340_command

    def b52_command(self):
        print("command")

    def b669_command(self):
        print("command")

    def b644_command(self):
        print("command")

    def b278_command(self):
        print("command")

    def b221_command(self):
        print("command")

    def b859_command(self):
        print("command")

    def b397_command(self):
        print("command")

    def b340_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
