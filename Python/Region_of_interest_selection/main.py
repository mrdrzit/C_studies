import tkinter as tk
from tkinter import filedialog

file_explorer = tk.Tk()
file_explorer.withdraw()
file_explorer.call("wm", "attributes", ".", "-topmost", True)
selected_files = filedialog.askopenfilename(title="Select the files to analyze", multiple=True)
selected_folder_to_save = filedialog.askdirectory(title="Select the folder to save the plots", mustexist=True)
experiments = []