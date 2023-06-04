import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    file_path = filedialog.askopenfilename(initialdir=os.path.expanduser("~"), title="Select File", filetypes=(("Python files", "*.py"), ("All files", "*.*")))
    if file_path:
        # Check if the file is hidden
        if os.path.basename(file_path).startswith('.'):
            print("Hidden file selected. Ignoring...")
        else:
            print("Selected file:", file_path)

root = tk.Tk()

open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

root.mainloop()
