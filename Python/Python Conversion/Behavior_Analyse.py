from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Define Settings")

def close_window():
    global plts, Exp_nm, Exp_tp, Frames, ArenaWidth, ArenaHeight
    plts = Exp_name.get()
    Exp_nm = Exp_type.get()
    Exp_tp = Plots.get()
    Frames = Fps.get()
    ArenaWidth = Arena_width.get()
    ArenaHeight = Arena_height.get()
    root.destroy()

root = Tk()
root.title("Define Settings")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
Btn = ttk.Button(mainframe, text="OK", command = close_window)
Btn.grid(column=9, row=9, sticky=E)


#TODO #5 Create an input dialog to "Define Settings"
#TODO #6 Import and organize files based on extension
#TODO #7 Create an imput dialog that defines "Figure Organization"