from scipy.stats import moyal
import matplotlib.pyplot as plt
import timeit
from methode_trapezes import trapeze
from methode_romberg import romberg
from portee import fun
import constantes

# Question 9

sample = moyal(loc=150, scale=4).rvs(size=10000)

plt.hist(sample)
plt.xlabel('Énergie cinétique initiale [MeV]')
plt.ylabel('Nombre de protons')
plt.show()

# Question 10

temps = 0
n = 0
for i in sample:
    if temps < 1:
        temps += timeit.timeit(trapeze(fun, 100, 0, Ti, "eau") * dens["eau"][1])
        n += 1
    
    