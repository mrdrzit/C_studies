from tkinter import *
from tkinter import ttk
import numpy as np

def close_window():
    global plts, Exp_nm, Exp_tp, Frames, ArenaWidth, ArenaHeight
    Exp_nm = Exp_name.get()
    Exp_tp = Exp_type.get()
    plts = Plots.get()
    Frames = Fps.get()
    ArenaWidth = Arena_width.get()
    ArenaHeight = Arena_height.get()
    root.destroy()
    input_settings = np.array([])
    return input_settings

root = Tk()
root.title("Define Settings")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Btn = ttk.Button(mainframe, text="OK", command = close_window)
Btn.grid(column=9, row=9, sticky=E)

Exp_name = ttk.Entry(mainframe, width=30)
Exp_name.insert(0, "Exp_")
Exp_name.grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="Experiment Name:").grid(column=1, row=1)

Exp_type = ttk.Entry(mainframe, width=6)
Exp_type.insert(0, "1")
Exp_type.grid(column=2, row=2, sticky=W)
ttk.Label(mainframe, text="Experiment Type (Type (1) to Open Field / Type (2) to Elevated plus maze):").grid(column=1, row=2)

Plots = ttk.Entry(mainframe, width=6)
Plots.insert(0, "1")
Plots.grid(column=2, row=3, sticky=W)
ttk.Label(mainframe, text="Plot Figures (Type (1) yes / Type (2) no):").grid(column=1, row=3)

Fps = ttk.Entry(mainframe, width=6)
Fps.insert(0, "30")
Fps.grid(column=2, row=4, sticky=W)
ttk.Label(mainframe, text="The vídeo is playing at How many frames per second?").grid(column=1, row=4)

Arena_width = ttk.Entry(mainframe, width=6)
Arena_width.insert(0, "65")
Arena_width.grid(column=2, row=5, sticky=W)
ttk.Label(mainframe, text="Arena size -> Width (cm):").grid(column=1, row=5)

Arena_height = ttk.Entry(mainframe, width=6)
Arena_height.insert(0, "65")
Arena_height.grid(column=2, row=6, sticky=W)
ttk.Label(mainframe, text="Arena size -> Height (cm):").grid(column=1, row=6)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

Exp_name.focus()
root.mainloop()

#TODO #6 Import and organize files based on extension
#TODO #7 Create an imput dialog that defines "Figure Organization"
#TODO #9 Separate the dialog creation from the main file to clean up the space a little