import os
import tkinter as tk
from tkinter import ttk

def get_file_properties(path):
    file_type = "File"
    if os.path.isdir(path):
        file_type = "Directory"
    date_modified = os.path.getmtime(path)
    size = os.path.getsize(path)
    return file_type, date_modified, size

def populate_treeview(parent, node):
    parent_node = treeview.insert(parent, 'end', text=node, open=False)
    file_type, date_modified, size = get_file_properties(node)
    treeview.set(parent_node, "Type", file_type)
    treeview.set(parent_node, "Date Modified", date_modified)
    treeview.set(parent_node, "Size", size)

root = tk.Tk()
treeview = ttk.Treeview(root, columns=("Type", "Date Modified", "Size"))
treeview.heading("#0", text="Name")
treeview.heading("Type", text="Type")
treeview.heading("Date Modified", text="Date Modified")
treeview.heading("Size", text="Size")
treeview.pack()

root_dir = os.getcwd()  # Replace with the desired directory path
populate_treeview('', root_dir)

root.mainloop()
