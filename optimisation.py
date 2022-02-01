from scipy.stats import moyal
import matplotlib.pyplot as plt


sample = moyal(loc=150, scale=4).rvs(size=10000)

plt.hist(sample)
plt.show()