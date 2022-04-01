import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Open_Field = "/home/state_orders/Documents/vscode/Code_studies/Python/Python Conversion/autoregressive_tests/OpenField.csv"
Plus_Maze = "/home/state_orders/Documents/vscode/Code_studies/Python/Python Conversion/autoregressive_tests/EPM.csv"

Data_Open_Field = pd.read_csv(Open_Field, header=None, delimiter=",", dtype={"0": np.float32, "1": np.float32})
Data_Plus_Maze = pd.read_csv(Plus_Maze, header=None, delimiter=",", dtype={"0": np.float32, "1": np.float32})



Data_Open_Field[0] = Data_Open_Field[0].interpolate()
Data_Open_Field[1] = Data_Open_Field[1].interpolate()
Data_Plus_Maze[0] = Data_Plus_Maze[0].interpolate()
Data_Plus_Maze[1] = Data_Plus_Maze[1].interpolate()


write = pd.DataFrame(Data_Open_Field)
writeEPM = pd.DataFrame(Data_Plus_Maze)

pd.DataFrame.to_csv(write, "/home/state_orders/Documents/vscode/Code_studies/Python/Python Conversion/autoregressive_tests/output.csv", header=0, index=0)
pd.DataFrame.to_csv(writeEPM, "/home/state_orders/Documents/vscode/Code_studies/Python/Python Conversion/autoregressive_tests/outputEPM.csv", header=0, index=0)

plt.plot(Data_Open_Field[0], Data_Open_Field[1])
plt.show()
plt.plot(Data_Plus_Maze[0], Data_Plus_Maze[1])
plt.show()
