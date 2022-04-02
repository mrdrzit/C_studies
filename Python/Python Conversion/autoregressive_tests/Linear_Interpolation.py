import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Open_Field = "/OpenField.csv"
Plus_Maze = "/EPM.csv"

Data_Open_Field = pd.read_csv(Open_Field, header=None, delimiter=",", dtype={"0": np.float32, "1": np.float32})
Data_Plus_Maze = pd.read_csv(Plus_Maze, header=None, delimiter=",", dtype={"0": np.float32, "1": np.float32})



Data_Open_Field[0] = Data_Open_Field[0].interpolate()
Data_Open_Field[1] = Data_Open_Field[1].interpolate()
Data_Plus_Maze[0] = Data_Plus_Maze[0].interpolate()
Data_Plus_Maze[1] = Data_Plus_Maze[1].interpolate()


write = pd.DataFrame(Data_Open_Field)
writeEPM = pd.DataFrame(Data_Plus_Maze)

pd.DataFrame.to_csv(write, "/output.csv", header=0, index=0)
pd.DataFrame.to_csv(writeEPM, "/outputEPM.csv", header=0, index=0)

plt.plot(Data_Open_Field[0], Data_Open_Field[1])
plt.show()
plt.plot(Data_Plus_Maze[0], Data_Plus_Maze[1])
plt.show()
