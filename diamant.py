import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T = [222.4, 262.4, 283.7, 306.4, 331.3, 358.5, 413.0, 479.2, 520.0, 879.7, 1079.7, 1258.0]
c = np.array([0.762, 1.146, 1.354, 1.582, 1.838, 2.118, 2.661, 3.280, 3.631, 5.290, 5.387, 5.507])*4.184

plt.scatter(T, c)

R = 8.314
def cvm(temp, theta):
    return 3*R * (theta/temp)**2 * np.exp(theta/temp) * (np.exp(theta/temp)-1)**(-2)

popt, pcov = curve_fit(cvm, T, c, p0=1300)
print(popt)
print(pcov)

T_teoretisk = np.linspace(1, 1300, 600)
plt.plot(T_teoretisk, cvm(T_teoretisk, popt[0]))

plt.ylim([0, 25])
plt.xlim([0, 1300])

plt.show()