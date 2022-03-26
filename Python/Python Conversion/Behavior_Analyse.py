from email import header
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from Settings_dialog import *
import pandas as pd

class Header:
  def __init__(self, Last_Frame, File_Info, File_Name_Csv, File_Name_Png):
    self.Last_Frame = Last_Frame
    self.File_Info = File_Info
    self.File_Name_Csv = File_Name_Csv
    self.File_Name_Png = File_Name_Png


create_Settings_dialog()


#TODO #6 Import and organize files based on extension
#TODO #7 Create an imput dialog that defines "Figure Organization"
#TODO #9 Separate the dialog creation from the main file to clean up the space a little