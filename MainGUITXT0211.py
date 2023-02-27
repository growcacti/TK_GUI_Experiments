import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from tkinter import messagebox
import pyautogui as pg
import pyperclip as pc
import sys

file_name = None
PROGRAM_NAME = "PyEditor"

root = Tk()
root.title("PyEditor")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


def quit():
    if tkinter.messagebox.askokcancel("Quit?", "Really quit?"):
        root.destroy()


def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    text.delete(1.0, END)


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
        text.delete(1.0, END)
        with open(file_name) as f:
            text.insert(1.0, f.read())


def save_file(event=None):
    global file_name
    if not file_name:
        save_as_file()
    else:
        write_to_file(file_name)
    return "break"


def save_as_file(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    )
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title("{} - {}".format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def write_to_file(file_name):
    try:
        content = text.get(1.0, "end")
        with open(file_name, "w") as the_file:
            the_file.write(content)
    except IOError:
        pass


def cut():
    text.event_generate("<<Cut>>")


def copy():
    text.event_generate("<<Copy>>")


def paste():
    text.event_generate("<<Paste>>")


def undo():
    text.event_generate("<<Undo>>")


def redo(event=None):
    text.event_generate("<<Redo>>")
    return "break"


def find(event=None):
    search_top_level = Toplevel(root)
    search_top_level.title("Find Text")
    search_top_level.transient(root)
    Label(search_top_level, text="Find All:").grid(row=0, column=0, sticky="e")
    search_entry_widget = Entry(search_top_level, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_top_level, text="Ignore Case", variable=ignore_case_value).grid(
        row=1, column=1, sticky="e", padx=2, pady=2
    )
    Button(
        search_top_level,
        text="Find All",
        underline=0,
        command=lambda: search_output(
            search_entry_widget.get(),
            ignore_case_value.get(),
            text,
            search_top_level,
            search_entry_widget,
        ),
    ).grid(row=2, column=2, sticky="e" + "w", padx=2, pady=2)

    def close_search_win():
        text.tag_remove("match", "1.0", END)
        search_top_level.destroy()
        search_top_level.protocol("WM_DELETE_win", close_search_win)
        return "break"


def search_output(needle, if_ignore_case, text, search_top_level, search_box):
    text.tag_remove("match", "1.0", END)
    matches_found = 0
    if needle:
        start_pos = "1.0"
        while True:
            start_pos = text.search(
                needle, start_pos, nocase=if_ignore_case, stopindex=END
            )
            if not start_pos:
                break
            end_pos = "{}+{}c".format(start_pos, len(needle))
            text.tag_add("match", start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
            text.tag_config("match", foreground="red", background="yellow")
            search_box.focus_set()
            search_top_level.title("{} matches found".format(matches_found))


def select_all(event=None):
    text.tag_add("sel", "1.0", "end")
    return "break"


def about():
    tkinter.messagebox.showinfo(
        "About",
        "{}{}".format(
            PROGRAM_NAME,
            "\nThis is a Text Editor application still in development JH APPS 2021",
        ),
    )


def help():
    tkinter.messagebox.showinfo("Help", "")


def show_info_bar():
    val = showinbar.get()
    if val:
        line_number_bar.pack(expand=NO, fill=None, side=RIGHT, anchor="se")
    elif not val:
        "<<ListboxSelect>>", line_number_bar.pack_forget()


def highlight_line(interval=100):
    text.tag_remove("active_line", 1.0, "end")
    text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    text.after(interval, toggle_highlight)


def undo_highlight():
    text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    val = hltln.get()
    undo_highlight() if not val else highlight_line()


def theme():
    global bgc, fgc
    val = themechoice.get()
    clrs = clrschms.get(val)
    fgc, bgc = clrs.split(".")
    fgc, bgc = "#" + fgc, "#" + bgc
    text.config(bg=bgc, fg=fgc)


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state="normal")
    line_number_bar.delete("1.0", "end")
    line_number_bar.insert("1.0", line_numbers)
    line_number_bar.config(state="disabled")


def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def show_cursor_info_bar():
    show_cursor_info_checked = showinbar.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand="no", fill=None, side="right", anchor="se")
    else:
        cursor_info_bar.pack_forget()


def get_line_numbers():
    output = ""
    if showinbar.get():
        row, col = text.index("end").split(".")
        for i in range(1, int(row)):
            output += str(i) + "\n"
    return output


def update_cursor_info_bar(event=None):
    row, col = text.index(INSERT).split(".")
    line_num, col_num = str(int(row)), str(int(col) + 1)
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


def cmd():
    pass


shortcutbar = Frame(root, height=10)


btn1 = Button(shortcutbar, text="NONE", command=cmd)
btn2 = Button(shortcutbar, text="2", command=cmd)
btn3 = Button(shortcutbar, text="3", command=cmd)
btn4 = Button(shortcutbar, text="4", command=cmd)
btn5 = Button(shortcutbar, text="5", command=cmd)
btn6 = Button(shortcutbar, text="6", command=cmd)
btn7 = Button(shortcutbar, text="7", command=cmd)
btn8 = Button(shortcutbar, text="8", command=cmd)
btn9 = Button(shortcutbar, text="9", command=cmd)

btn1.pack(side=RIGHT)
btn2.pack(side=RIGHT)
btn3.pack(side=RIGHT)
btn4.pack(side=RIGHT)
btn5.pack(side=RIGHT)
btn6.pack(side=RIGHT)
btn7.pack(side=RIGHT)
btn8.pack(side=RIGHT)
btn9.pack(side=RIGHT)
shortcutbar.pack(expand=False, fill=X)
menubar = Menu(root)

text = Text(root, wrap="word", undo=1)
text.bind("<Control-y>", redo)
text.bind("<Control-Y>", redo)
text.bind("<Control-A>", select_all)
text.bind("<Control-a>", select_all)

import tkinter.messagebox as messagebox
import subprocess

text.bind("<Control-f>", find)
text.bind("<Control-F>", find)
text.bind("<Control-f>", find)
text.bind("<Control-F>", find)
text.bind("<Control-o>", open_file)
text.bind("<Control-O>", open_file)
text.bind("<Control-s>", save_file)
text.bind("<Control-S>", save_file)
text.bind("<Shift-Control-S>", save_as_file)
text.bind("<Shift-Control-s>", save_as_file)
text.bind("<Control-n>", new_file)
text.bind("<Control-N>", new_file)
text.bind("<KeyPress-F1>", help)
text.bind("<Any-KeyPress>", on_content_changed)
text.bind("<Button-3>", show_popup_menu)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(
    label="New", accelerator="Ctrl+N", compound="left", underline=0, command=new_file
)
file_menu.add_command(
    label="Open", accelerator="Ctrl+O", compound="left", underline=0, command=open_file
)
file_menu.add_command(
    label="Save", accelerator="Ctrl+S", compound="left", underline=0, command=save_file
)
file_menu.add_command(
    label="Save As",
    accelerator="Shift+Ctrl+S",
    compound="left",
    underline=0,
    command=save_as_file,
)
file_menu.add_command(
    label="Exit", accelerator="Alt+F4", compound="left", underline=0, command=quit
)
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(
    label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=cut
)
edit_menu.add_command(
    label="Copy", accelerator="Ctrl+C", compound="left", underline=0, command=copy
)
edit_menu.add_command(
    label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=paste
)
edit_menu.add_command(
    label="Undo", accelerator="Ctrl+Z", compound="left", underline=0, command=undo
)
edit_menu.add_command(
    label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=redo
)
edit_menu.add_command(
    label="Find", accelerator="Ctrl+F", compound="left", underline=0, command=find
)
edit_menu.add_command(
    label="Select All",
    accelerator="Ctrl+A",
    compound="left",
    underline=7,
    command=select_all,
)
menubar.add_cascade(label="Edit", menu=edit_menu)

view_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)
showln = IntVar()
showln.set(1)
view_menu.add_checkbutton(label="Show Line Number", variable=showln)
showinbar = IntVar()
showinbar.set(1)
view_menu.add_checkbutton(
    label="Show Info Bar at Bottom", variable=showinbar, command=show_info_bar
)
hltln = IntVar()
view_menu.add_checkbutton(
    label="Highlight Current Line", variable=hltln, command=toggle_highlight
)
themes_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Themes", menu=themes_menu)
clrschms = {
    "1. Default White": "000000.FFFFFF",
    "2. Greygarious Grey": "83406A.D1D4D1",
    "3. Lovely Lavender": "202B4B.E1E1FF",
    "4. Aquamarine": "5B8340.D1E7E0",
    "5. Bold Beige": "4B4620.FFF0E1",
    "6. Cobalt Blue": "ffffBB.3333aa",
    "7. Olive Green": "D1E7E0.5B8340",
}
themechoice = StringVar()
themechoice.set("1. Default White")
for k in sorted(clrschms):
    themes_menu.add_radiobutton(label=k, variable=themechoice, command=theme)

about_menu = Menu(menubar, tearoff=0)
about_menu.add_command(label="About", compound="left", underline=0, command=about)
about_menu.add_command(label="Help", compound="left", underline=0, command=help)
menubar.add_cascade(label="About", menu=about_menu)

cursor_info_bar = Label(text, text="Line: 1 | Column: 1")
cursor_info_bar.pack(expand=NO, fill=None, side=RIGHT, anchor="se")

shortcut_bar = Frame(root, height=25, background="light sea green")
shortcut_bar.pack(expand="no", fill="x")

line_number_bar = Text(
    root,
    width=4,
    padx=3,
    takefocus=0,
    border=0,
    background="khaki",
    state="disabled",
    wrap="none",
)
line_number_bar.pack(side="left", fill="y")

view_menu.add_checkbutton(
    label="Show Cursor Location at Bottom",
    variable=showinbar,
    command=show_cursor_info_bar,
)

popup_menu = Menu(text)
for i in ("cut", "copy", "paste", "undo", "redo"):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound="left", command=cmd)
    popup_menu.add_separator()
    popup_menu.add_command(label="Select All", underline=7, command=select_all)

scroll_bary = Scrollbar(text)
scroll_bary.config(command=text.yview)
scroll_bary.pack(side="right", fill="y")

text.pack(expand="yes", fill="both")
text.configure(yscrollcommand=scroll_bary.set)

root.protocol("WM_DELETE_win", quit)
root.config(menu=menubar)
geo = root.geometry
geo("400x400+400+400")
root["bg"] = "orange"

# get the list of files
flist = os.listdir()

lbox = tk.Listbox(root)
lbox.pack(side=RIGHT)

# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)


def showcontent(event, audio=0):
    x = lbox.curselection()[0]
    file = lbox.get(x)
    with open(file, "r", encoding="utf-8") as file:
        file = file.read()
    text.delete("1.0", tk.END)
    text.insert(tk.END, file)


def txtt():
    txt(text.get("1.0", tk.INSERT))


def opensystem(event):
    x = lbox.curselection()[0]
    os.system(lbox.get(x))
    with open(file, "r", encoding="utf-8") as file:
        file = file.read()
    text.delete("1.0", tk.END)
    text.insert(tk.END, file)


text = tk.Text(root, bg="cyan")
text.pack()
# BINDING OF LISTBOX lbox
lbox.bind("<<ListboxSelect>>", showcontent)
lbox.bind("<Double-Button-1>", opensystem)
# BUTTON


root.mainloop()
#
