"""
Exercise:
Write a function temp_stat(temps) to compute the average, median, standard 
deviation and variance of the temperatures in the table.  Print each out.
The following code generates the same temperatures each time because the seed 
is set. Print the temperature list as the first line of the function.

Here is what my run on the table of temperatures built below looks like:

temp_stat(temperatures)
[52, 61, 45, 50, 44, 34, 57, 80, 91, 50, 38, 91, 84, 20, 55, 23, 83, 42, 44, 84]
Mean:  56.4
Median:  51.0
Standard deviation:  22.04397518836526
Variance:  485.9368421052631

"""
#%%
import random
from statistics import stdev, variance
random.seed(77)
temperatures = []
for i in range(0,20):
    temperatures.append(random.randint(20,95))

#%%
def temp_stat(temps):
    """ prints the average, median, std dev, and variance of temps """
    import statistics as math

    print(temps)
    print(math.mean(temps))
    print(math.median(temps))
    print(math.stdev(temps))
    print(math.variance(temps))
    try:
        print(math.mode(temps))
    except Exception as e:
        print(e)
    

#%%