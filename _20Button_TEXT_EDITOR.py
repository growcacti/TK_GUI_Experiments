
# get the list of files
flist = os.listdir()

lbox = tk.Listbox(top)
lbox.pack(side=RIGHT)

# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)
 
 
