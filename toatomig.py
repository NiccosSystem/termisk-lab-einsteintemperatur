import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T = [100, 200, 250, 298, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]
c = np.array([29.114, 29.685, 30.447, 31.302, 31.336, 32.207, 32.992, 33.674, 34.255, 35.166,
     35.832, 36.336, 36.732, 37.057, 37.334, 37.579, 37.802, 38.008]) - 8.314

plt.scatter(T, c)

R = 8.314
def cvm(temp, theta, k, m):
    return m * 3*R * (theta/temp)**2 * np.exp(theta/temp) * (np.exp(theta/temp)-1)**(-2) + k

popt, pcov = curve_fit(cvm, T, c, p0=[250, 2, 0.3])
print(popt)
print(pcov)

T_teoretisk = np.linspace(1, 1500, 600)
plt.plot(T_teoretisk, cvm(T_teoretisk, *popt))

plt.ylim([0, 31])
plt.xlim([0, 1450])

plt.show()