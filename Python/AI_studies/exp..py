import matplotlib.pyplot as plt
import numpy as np

data = range(-10, 10)
exp = []

for x in data:
    exp.append(x / (1 + np.exp(-x)))


plt.plot(exp)
plt.show()
pass
