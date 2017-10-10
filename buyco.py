import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 273.15, 298.15, 300, 350, 400, 450, 500, 550, 600, 650,
     700, 750, 800, 850, 900]
c = np.array([3.269/1000, 1.992/100, 7.608/100, 1.848/10, 3.371/10, 5.097/10, 6.851/10, 8.536/10, 1.010, 1.152, 1.655,
              1.922, 2.070, 2.116, 2.156, 2.159, 2.222, 2.273, 2.321, 2.370, 2.421, 2.478, 2.539,
              2.606, 2.679, 2.758, 2.844, 2.935])*4.184*26.98/10

plt.scatter(T, c)

R = 8.314
def cvm(temp, theta):
    return 3*R * (theta/temp)**2 * np.exp(theta/temp) * (np.exp(theta/temp)-1)**(-2)

popt, pcov = curve_fit(cvm, T, c, p0=300)
print(popt)
print(pcov)

T_teoretisk = np.linspace(1, 960, 600)
plt.plot(T_teoretisk, cvm(T_teoretisk, popt[0]))

plt.ylim([0, 34])
plt.xlim([0, 950])

plt.show()