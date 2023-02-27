from tkinter import *




root = Tk()
root.title("Sin Wave")
root.geometry('600x550')

# A sin (wt + b)
amplitude = 1
frequency = 1
vertical_shift = 0
phase_shift = 0

# Amplitude
Label(root, text = "Amplitude").grid(row=0, column=0)
amplitude_entry = Entry(root, width = 5)
amplitude_entry.grid(row=0, column = 1)

# Frequency
Label(root, text = "Frequency").grid(row=1, column=0)
frequency_entry = Entry(root, width = 5)
frequency_entry.grid(row=1, column=1)

# Vertical Shift
Label(root, text = "Vertical Shift").grid(row=2, column=0)
vertical_shift_entry = Entry(root, width = 5)
vertical_shift_entry.grid(row=2, column=1)

# Horizontal Shift
Label(root, text = "Phase Shift").grid(row=3, column=0)
phase_shift_entry = Entry(root, width = 5)
phase_shift_entry.grid(row=3, column=1)

# Update Button
button1 = Button(root, text="Calculate", command = update_values)
button1.grid(row=4, column=0)
root.bind("<Return>", update_values)
plot_values()
pass
t = []
for x in list(range(0,101)):
	t.append(x/15.87)
	
def update_values( event=None):
    return None
	
def plot_values():
		
    return None
	

