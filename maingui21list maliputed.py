import string
import itertools
import re
import sys


import tkinter as tk

from tkinter import ttk

#HEAD

from tkinter import *

from tkinter import filedialog, messagebox

import os
verbs = ['Freeze', 'Give' , 'Go', 'Grow', 'Hide', 'Know', 'Lie', 'Mistake','Mow', 'Overdraw', 'Overtake', 'Re-prove', 'Ride', 'Ring', 'Rise', 'Saw', 'See', 'Sew', 'Shake', 'Shave', 'Show', 'Shrink', 'Slay']
verb2 = ['Sow','Speak', 'Spin','Spit', 'Split', 'Spoil', 'Spread', 'Spring' ,'Stand' ,'Steal', 'Stride', 'Strike',  'Swear', 'Swell', 'Swim' ,'Take', 'Thrive' ,'Throw', 'Tread' ,'Undergo' ,'Undertake', 'Wake'] 



def reversrstr():
    w_str1 = contect_text.get("1.0", END)
    w_str2 = w_str1[::-1]
    content_text.insert(END, w_str2[::-1])

def squ_num():
    
    squares = (x**2 for x in itertools.count(1))


    for x in squares:
        print(x)
        content_text.insert(END, x)
        if x > 500:
            squares.close()


def lo():
     wstr = content_text.get("1.0", END)
     wstr.lower()
     content_text.insert(END, wstr)


def lc():
    wstr = content_text.get("1.0", END)
    wstr.lower()
    contect_text.insert(END, wstr)



def up():
    wstr = content_text.get("1.0", END)
    wstr.upper()
    content_text.insert(END, wstr)
    
    
           

def tc():
    wstr = content_text.get("1.0", END)
    wstr.title()
    content_text.insert(END, wstr)
      
def cleartxt():
    content_text.delete("1.0", tk.END)

def letterlc():
    def letters():
        for c in string.ascii_lowercase:
            yield c

    for letter in letters():
        
        content_text.insert(END, letter)
    

def listshow():
    content_text.insert(1.0, verbs)


def listsort():
    content_text.insert(1.0, verbs.sort)
     

root = tk.Tk()

root.title("TXT edit 20 BTN JH Special APP")
root.geometry("1000x1000")
file_name=None

PROGRAM_NAME="PyEditor"

# There are 20 buttons that can be used to call added functions
# The Button Bar
        



def quit():

    if tk.messagebox.askokcancel("Quit?", "Really quit?"):

       
        root.destory()

 

def new_file(event=None):

    root.title("Untitled")

    global file_name

    file_name = None

    content_text.delete(1.0,END)

 

def open_file(event=None):

    input_file_name=tk.filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

    if input_file_name:

        global file_name

        file_name=input_file_name

        root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))

        content_text.delete(1.0,END)

        with open(file_name) as f:

            content_text.insert(1.0,f.read())

 

def save_file(event=None):

    global file_name

    if not file_name:

        save_as_file()

    else:

        write_to_file(file_name)

    return "break"

 

def save_as_file(event=None):

    input_file_name = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

    if input_file_name:

        global file_name

        file_name = input_file_name

        write_to_file(file_name)

        root.title('{} - {}'.format(os.path.basename(file_name),PROGRAM_NAME))

    return "break"

 

def write_to_file(file_name):

    try:

        content = content_text.get(1.0, 'end')

        with open(file_name, 'w') as the_file:

            the_file.write(content)

    except IOError:

        pass

 

def cut():

    content_text.event_generate("<<Cut>>")

 

def copy():

    content_text.event_generate("<<Copy>>")

 

def paste():

    content_text.event_generate("<<Paste>>")

 

def undo():

    content_text.event_generate("<<Undo>>")

 

def redo(event=None):

    content_text.event_generate("<<Redo>>")

    return 'break'

 

def find(event=None):

    search_top_level=Toplevel(root)

    search_top_level.title("Find Text")

    search_top_level.transient(root)

    Label(search_top_level,text="Find All:").grid(row=0,column=0,sticky='e')

    search_entry_widget=Entry(search_top_level,width=25)

    search_entry_widget.grid(row=0,column=1,padx=2,pady=2,sticky='we')

    search_entry_widget.focus_set()

    ignore_case_value=IntVar()

    Checkbutton(search_top_level, text='Ignore Case',variable=ignore_case_value).grid(row=1, column=1, sticky='e', padx=2, pady=2)

    Button(search_top_level,text="Find All",underline=0,command=lambda:search_output(search_entry_widget.get("1.0", END),ignore_case_value.get("1.0", END),content_text,search_top_level,search_entry_widget)).grid(row=2,column=2,sticky='e'+'w',padx=2,pady=2)

    def close_search_r():

        content_text.tag_remove('match','1.0',END)

        search_top_level.destroy()

        search_top_level.protocol('WM_DELETE_WINDOW',close_search_root)

        return 'break'

 

def search_output(needle,if_ignore_case,content_text,search_top_level,search_box):

    content_text.tag_remove('match','1.0',END)

    matches_found=0

    if needle:

        start_pos='1.0'

        while True:

            start_pos=content_text.search(needle,start_pos,nocase=if_ignore_case,stopindex=END)

            if not start_pos:

                break

            end_pos='{}+{}c'.format(start_pos,len(needle))

            content_text.tag_add('match',start_pos,end_pos)

            matches_found+=1

            start_pos=end_pos

            content_text.tag_config('match',foreground='red',background='yellow')

            search_box.focus_set()

            search_top_level.title('{} matches found'.format(matches_found))

 

def select_all(event=None):

    content_text.tag_add('sel', '1.0', 'end')

    return "break"

 

def about():

    tk.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\nThis is a Text Editor application still in development JH APPS 2021"))

def help():

    tk.messagebox.showinfo("Help", "")

               

def show_info_bar():

    val = showinbar.get("1.0", END)

    if val:

        line_number_bar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')

    elif not val:

        line_number_bar.pack_forget()

 

def highlight_line(interval=100):

    content_text.tag_remove("active_line", 1.0, "end")

    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")

    content_text.after(interval, toggle_highlight)

 

def undo_highlight():

    content_text.tag_remove("active_line", 1.0, "end")

 

def toggle_highlight(event=None):

    val = hltln.get("1.0", END)

    undo_highlight() if not val else highlight_line()

 

def theme():

        global bgc,fgc

        val = themechoice.get("1.0", END)

        clrs = clrschms.get(val)

        fgc, bgc = clrs.split('.')

        fgc, bgc = '#'+fgc, '#'+bgc

        content_text.config(bg=bgc, fg=fgc)

 

def update_line_numbers(event = None):

    line_numbers = get_line_numbers()

    line_number_bar.config(state='normal')

    line_number_bar.delete('1.0', 'end')

    line_number_bar.insert('1.0', line_numbers)

    line_number_bar.config(state='disabled')

 

def on_content_changed(event=None):

    update_line_numbers()

    update_cursor_info_bar()

 

def show_cursor_info_bar():

    show_cursor_info_checked = showinbar.get("1.0", END)

    if show_cursor_info_checked:

        cursor_info_bar.pack(expand='no', fill=None, side='right',anchor='se')

    else:

        cursor_info_bar.pack_forget()

 

def get_line_numbers():

    output = ''

    if showinbar.get("1.0", END):

        row, col = content_text.index("end").split('.')

        for i in range(1, int(row)):

            output += str(i)+ '\n'

    return output

 

def update_cursor_info_bar(event=None):

    row, col = content_text.index(INSERT).split('.')

    line_num, col_num = str(int(row)), str(int(col)+1)

    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)

    cursor_info_bar.config(text=infotext)

def com():
    pass

def show_popup_menu(event):

    popup_menu.tk_popup(event.x_root, event.y_root)

 

shortcutbar = Frame(root, height=25)

#icons = {'new_file':'new_file','open_file':'open_file','save_file':'save','cut':'Cut','copy':'Copy','paste':'Paste',"undo":'Undo','redo':'Redo',"find":'on_find',"about":'about'}

#for f,icon in icons.items():

 

#cmd = eval(f)
cmd = com
btn1 = Button(shortcutbar, text="show list", command=listshow)
btn1.pack(side=LEFT)
btn2 = Button(shortcutbar, text="sort", command=listsort)
btn2.pack(side=LEFT)
btn3 = Button(shortcutbar, text="Clear", command=cleartxt)
btn3.pack(side=LEFT)
btn4 = Button(shortcutbar, text="square", command=squ_num)
btn4.pack(side=LEFT)
btn5 = Button(shortcutbar, text="Reversal", command=cmd)
btn5.pack(side=LEFT)
btn6 = Button(shortcutbar, text="Lowercase", command=lo)
btn6.pack(side=LEFT)
btn7 = Button(shortcutbar, text="Uppercase", command=up)
btn7.pack(side=LEFT)
btn8 = Button(shortcutbar, text="cv_chop.py", command=cmd)
btn8.pack(side=LEFT)
btn9 = Button(shortcutbar, text="9", command=cmd)
btn9.pack(side=LEFT)
btna = Button(shortcutbar, text="10", command=cmd)
btna.pack(side=LEFT)
btnb = Button(shortcutbar, text="11", command=cmd)
btnb.pack(side=LEFT)
btnc = Button(shortcutbar, text="12", command=cmd)
btnc.pack(side=LEFT)
btnd = Button(shortcutbar, text="13", command=cmd)
btnd.pack(side=LEFT)
btne = Button(shortcutbar, text="14", command=cmd)
btne.pack(side=LEFT)
btnf = Button(shortcutbar, text="15", command=cmd)
btnf.pack(side=LEFT)
btng = Button(shortcutbar, text="16", command=cmd)
btng.pack(side=LEFT)
btnh = Button(shortcutbar, text="17", command=cmd)
btnh.pack(side=LEFT)
btni = Button(shortcutbar, text="18", command=cmd)
btni.pack(side=LEFT)
btnj = Button(shortcutbar, text="19", command=cmd)
btnj.pack(side=LEFT)
btnk = Button(shortcutbar, text="20", command=cmd)
btnk.pack(side=LEFT)
shortcutbar.pack(expand=NO, fill=X)

 

 

menubar = Menu(root)

 

content_text = Text(root, wrap='word',undo=1)

content_text.bind('<Control-y>', redo)

content_text.bind('<Control-Y>', redo)

content_text.bind('<Control-A>', select_all)

content_text.bind('<Control-a>', select_all)

content_text.bind('<Control-f>', find)

content_text.bind('<Control-F>', find)

content_text.bind('<Control-f>', find)

content_text.bind('<Control-F>', find)

content_text.bind('<Control-o>', open_file)

content_text.bind('<Control-O>', open_file)

content_text.bind('<Control-s>', save_file)

content_text.bind('<Control-S>', save_file)

content_text.bind('<Shift-Control-S>', save_as_file)

content_text.bind('<Shift-Control-s>', save_as_file)

content_text.bind('<Control-n>', new_file)

content_text.bind('<Control-N>', new_file)

content_text.bind('<KeyPress-F1>', help)

content_text.bind('<Any-KeyPress>', on_content_changed)

content_text.bind('<Button-3>', show_popup_menu)

 

file_menu = Menu(menubar,tearoff=0)

file_menu.add_command(label="New",accelerator='Ctrl+N',compound='left',underline=0,command=new_file)

file_menu.add_command(label="Open",accelerator='Ctrl+O',compound='left',underline=0,command=open_file)

file_menu.add_command(label="Save",accelerator='Ctrl+S',compound='left',underline=0,command=save_file)

file_menu.add_command(label="Save As",accelerator='Shift+Ctrl+S',compound='left',underline=0,command=save_as_file)

file_menu.add_command(label="Exit",accelerator='Alt+F4',compound='left',underline=0,command=quit)

menubar.add_cascade(label='File',menu=file_menu)

 

edit_menu=Menu(menubar,tearoff=0)

edit_menu.add_command(label="Cut",accelerator="Ctrl+X",compound='left',underline=0,command=cut)

edit_menu.add_command(label="Copy",accelerator="Ctrl+C",compound='left',underline=0,command=copy)

edit_menu.add_command(label="Paste",accelerator="Ctrl+V",compound='left',underline=0,command=paste)

edit_menu.add_command(label="Undo",accelerator="Ctrl+Z",compound='left',underline=0,command=undo)

edit_menu.add_command(label="Redo",accelerator="Ctrl+Y",compound='left',underline=0,command=redo)

edit_menu.add_command(label="Find",accelerator="Ctrl+F",compound='left',underline=0,command=find)

edit_menu.add_command(label="Select All",accelerator="Ctrl+A",compound='left',underline=7,command=select_all)

menubar.add_cascade(label="Edit",menu=edit_menu)

 

view_menu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="View", menu=view_menu)

showln = IntVar()

showln.set(1)

view_menu.add_checkbutton(label="Show Line Number", variable=showln)

showinbar = IntVar()

showinbar.set(1)

view_menu.add_checkbutton(label="Show Info Bar at Bottom", variable=showinbar, command=show_info_bar)

hltln = IntVar()

view_menu.add_checkbutton(label="Highlight Current Line", variable=hltln, command=toggle_highlight)

themes_menu = Menu(view_menu, tearoff=0)

view_menu.add_cascade(label="Themes", menu=themes_menu)

clrschms = {

'1. Blue': 'ffffBB.3333aa',

'2. Greygarious Grey':'83406A.D1D4D1',

'3. Lovely Lavender':'202B4B.E1E1FF' ,

'4. Aquamarine': '5B8340.D1E7E0',

'5. Bold Beige': '4B4620.FFF0E1',

'6. Cobalt Blue':'ffffBB.3333aa',

'7. Olive Green': 'D1E7E0.5B8340',

}

themechoice= StringVar()

themechoice.set('6. Cobalt Blue')

for k in sorted(clrschms):

    themes_menu.add_radiobutton(label=k, variable=themechoice, command=theme)

 

about_menu=Menu(menubar,tearoff=0)

about_menu.add_command(label="About",compound='left',underline=0,command=about)

about_menu.add_command(label="Help",compound='left',underline=0,command=help)

menubar.add_cascade(label="About",menu=about_menu)

 

cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')

cursor_info_bar.pack(expand=NO, fill=None, side=RIGHT,anchor='se')

 

shortcut_bar = Frame(root, height=25, background='light sea green')

shortcut_bar.pack(expand='no', fill='x')

 

line_number_bar = Text(root, width=4, padx=3, takefocus=0,border=0,background='khaki', state='disabled', wrap='none')

line_number_bar.pack(side='left', fill='y')

 

view_menu.add_checkbutton(label='Show Cursor Location at Bottom',variable=showinbar, command=show_cursor_info_bar)

 

popup_menu = Menu(content_text)

for i in ('cut', 'copy', 'paste', 'undo', 'redo'):

    cmd = eval(i)

    popup_menu.add_command(label=i, compound='left', command=cmd)

    popup_menu.add_separator()

popup_menu.add_command(label='Select All', underline=7,command=select_all)

 

scroll_bary = Scrollbar(content_text)

scroll_bary.config(command=content_text.yview)

scroll_bary.pack(side='right', fill='y')

 

content_text.pack(expand='yes', fill='both')

content_text.configure(yscrollcommand=scroll_bary.set)

 

root.protocol('WM_DELETE_r',quit)

root.config(menu=menubar)


#



 

 

def get_line_numbers():

    output = ''

    if showinbar.get("1.0", END):

        row, col = content_text.index("end").split('.')

        for i in range(1, int(row)):

            output += str(i)+ '\n'

    return output

 

def update_cursor_info_bar(event=None):

    row, col = content_text.index(INSERT).split('.')

    line_num, col_num = str(int(row)), str(int(col)+1)

    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)

    cursor_info_bar.config(text=infotext)

 

def show_popup_menu(event):

    popup_menu.tk_popup(event.x_root, event.y_root)

 


root.mainloop()

 

 
