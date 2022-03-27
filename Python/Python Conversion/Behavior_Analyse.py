from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from Settings_dialog import *
from Video_Analyse import *
from Plot_EPM import *
from skimage import io 
import pandas as pd
import numpy as np
import os

class Header:
  def __init__(self, Last_Frame, File_Path, File_Name_Csv, File_Name_Png):
    self.Last_Frame = Last_Frame
    self.File_path = File_Path # Equivalent to "header.FilePattern"
    self.File_Name_Csv = File_Name_Csv
    self.File_Name_Png = File_Name_Png


Input_Settings = Create_Settings_Dialog()

root = Tk() # Create a mainframe window
root.withdraw() # Hide mainframe to avoid a duplicate file selection window
                # Needed here because the "askopenfiles" opens a system windows to ask for file selection
FileName = fd.askopenfiles(title="Select the CSV and PNG files generated by the BONSAI software",filetypes=[("png and csv files","*")])
root.destroy()  # Delete mainframe

Data = [None] * (len(FileName)) # Initialize the data struct with the number of files loaded 
File_Header = Header([None],[None],[None]*len(FileName),[None]*len(FileName)) # Initialize the attributes of header with the number of files loaded
                                                                       # In this assignment, only "Last_Frame" and "File_Path", are not being
                                                                       # Preallocated. This is because in this instance of the code, the path
                                                                       # is being stored as a simple string, without anymore info about the image.
                                                                       # However, the "Last_Frame" was yielding an error where the empty values
                                                                       # cleanup was outputting "The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()"
                                                                       # See "https://researchdatapod.com/python-valueerror-the-truth-value-of-an-array-with-more-than-one-element-is-ambiguous-use-a-any-or-a-all/" for more info
                                                                       # The method used is comparing each value to a boolean "None".

# Loop through all files and convert the table data into a DataFrame (Basically a Pandas Table)
for file in range(0, len(FileName)):
  if file == 0:
    File_Header.File_path = FileName[file].name
    
  if FileName[file].name.endswith(".csv"):
    Data[file] = pd.read_csv(FileName[file].buffer, header=None, delimiter=",", dtype={"0": np.float32, "1": np.float32, "2": np.intc, "3": np.intc, "4": np.intc, "5": np.intc, "6": np.intc})
    File_Header.File_Name_Csv[file] = os.path.basename(FileName[file].name)
    print("Reading", File_Header.File_Name_Csv[file])

  elif FileName[file].name.endswith(".png"):
    File_Header.File_Name_Png[file] = os.path.basename(FileName[file].name)
    Gray_Image = io.imread(FileName[file].name, as_gray=1)
    File_Header.Last_Frame.append(Gray_Image)
    print("Reading", File_Header.File_Name_Png[file])

# Cleanup the empty values in the srtuct attributes
File_Header.File_Name_Csv = list(filter(None, File_Header.File_Name_Csv))
File_Header.File_Name_Png = list(filter(None, File_Header.File_Name_Png))

Plot_Settings = Create_Plots_Dialog()

## Function Calls

Video_Analyse(input_settings,File_Header,Data)

# [analyse,header,data] = Video_Analyse(input_settings,header,data);

# if     str2num(input_settings{2, 1}) == 1 && str2num(input_settings{3, 1}) == 1
#        plot_openfield;

# elseif str2num(input_settings{2, 1}) == 2 && str2num(input_settings{3, 1}) == 1
#        plot_EPM;
       
# end
#TODO #9 Separate the dialog creation from the main file to clean up the space a little