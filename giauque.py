import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

T = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
     150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 298, 300]
c = np.array([0.022, 0.054, 0.112, 0.203, 0.332, 0.500, 0.698, 0.912, 1.375, 1.846, 2.298, 2.714, 3.094, 3.422,
              3.704, 3.943, 4.165, 4.361, 4.536, 4.690, 4.823, 4.938, 5.039, 5.122, 5.198, 5.268,
              5.329, 5.383, 5.436, 5.483, 5.523, 5.562, 5.592, 5.599])*4.184

plt.scatter(T, c, color="0")

R = 8.314
def cvm(temp, theta):
    return 3*R * (theta/temp)**2 * np.exp(theta/temp) * (np.exp(theta/temp)-1)**(-2)

popt, pcov = curve_fit(cvm, T, c, p0=300)
print(popt)
print(pcov)

T_teoretisk = np.linspace(1, 330, 600)
plt.plot(T_teoretisk, cvm(T_teoretisk, popt[0]), color="0")

#plt.title(r"Kurvetilpasning, Giauque og Meads, $\Theta_E = 283$K")
plt.xlabel(r"$T$ / K")
plt.ylabel(r"$C_{vm}$ / J K$^{-1}$ mol $^{-1}$")

plt.ylim([0, 25])
plt.xlim([0, 320])

plt.tight_layout()

plt.show()

# VELGER T = 283.2K SOM EINSTEINTEMPERATUR FOR ALUMINIUM