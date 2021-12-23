#%%
import numpy as np
import matplotlib.pyplot as plt

# Fórmula >>> y(t) = Asin(2PI * f * t + PHI)
Fs = 1000;    # Amostragem
dt = 1/Fs;    # seconds per sample
Time = 3;     # seconds
timeVector = np.linspace(0, Time, int(Fs*Time), endpoint=False)
freqvector = np.arange(0,10,1)

def createWave(A, F, T):
    y = A * np.sin(2 * np.pi * F * timeVector)
    return y

a = createWave(1,2,timeVector)
b = createWave(2,4,timeVector)
c = createWave(5,6,timeVector)
d = np.add(a,b)

plt.subplot(5,1,1)
plt.plot(timeVector,a)
plt.subplot(5,1,2)
plt.plot(timeVector,b)
plt.subplot(5,1,3)
plt.plot(timeVector,c)
plt.subplot(5,1,4)
plt.plot(timeVector,d)