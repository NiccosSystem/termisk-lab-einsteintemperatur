import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fsolve
import math

ts1 = np.array([0, 60, 120, 180, 240])
ms1 = [50.20, 48.28, 46.47, 44.71, 42.97]

ts2 = np.array([360, 420, 480, 540, 600])
ms2 = np.array([41.36, 39.78, 38.23, 36.70, 35.22])-6.141

plt.scatter(ts1, ms1, label="Målepunkter", color="0")
plt.scatter(ts2, ms2, color="0")

plt.axvline(270, linestyle="dotted", color="0.3")
plt.text(274, 29, r"$t_1$")
plt.axvline(321, linestyle="dotted", color="0.3")
plt.text(325, 29, r"$t_2$")


def massefunk(tid, a, b):
    return a*tid + b


popts1, pcovs1 = curve_fit(massefunk, ts1, ms1)
popts2, pcovs2 = curve_fit(massefunk, ts2, ms2)

print("m1: Stigning: {0}   |    Konstantledd: {1}".format(*popts1))
print("m2: Stigning: {0}   |    Konstantledd: {1}".format(*popts2))

dm1 = massefunk(270, *popts1) - massefunk(270, *popts2)
dm2 = massefunk(321, *popts1) - massefunk(321, *popts2)

snitt_dm = 0.5 * (dm1+dm2)
usikker_dm = 0.5 * (dm1 - dm2)

print("Delta m1: {0}".format(dm1))
print("Delta m2: {0}".format(dm2))

print("Snitt deltaM: {0}".format(snitt_dm))
print("Usikkerhet deltaM: {0}".format(usikker_dm))

L = 2.0 * 10**5
T0 = 298.15
Tf = 77
n = 0.2223
R = 8.314
deltaQ = - snitt_dm * L / 1000
def epsilon(y):
    return y/(math.exp(y) - 1)

def deltaqfunk(theta):
    return 3 * n * R * (T0*epsilon(theta/T0) - Tf*epsilon(theta/Tf)) + deltaQ

einsteintemp = fsolve(deltaqfunk, 283)

print("Einsteintemperatur: {0}".format(einsteintemp))



ts1_space = np.linspace(0, 321, 600)
ts2_space = np.linspace(270, 600, 600)

plt.plot(ts1_space, massefunk(ts1_space, *popts1), color="0", label=r"$m_1(t)$")
plt.plot(ts2_space, massefunk(ts2_space, *popts2), color="0", label=r"$m_2(t)$", linestyle="--")

plt.xlabel(r"$t$ / s")
plt.ylabel(r"$m$ / g")
#plt.title(r"Eksperimentelle måleverdier og kurvetilpasning")

plt.tight_layout()
plt.legend()
plt.show()