from scipy.optimize import fsolve, curve_fit
import math
import numpy as np

ts1 = np.array([0, 60, 120, 180, 240])
ms1 = [50.20, 48.28, 46.47, 44.71, 42.97]

ts2 = np.array([360, 420, 480, 540, 600])
ms2 = np.array([41.36, 39.78, 38.23, 36.70, 35.22])-6.141

def massefunk(tid, a, b):
    return a*tid + b

popts1, pcovs1 = curve_fit(massefunk, ts1, ms1)
popts2, pcovs2 = curve_fit(massefunk, ts2, ms2)

dm1 = massefunk(270, *popts1) - massefunk(270, *popts2)
dm2 = massefunk(321, *popts1) - massefunk(321, *popts2)

snitt_dm = 0.5 * (dm1+dm2)

L = 2.0 * 10**5
T0r = 298.15
Tf = 77
n = 0.2223
n = 5.997 / 26.98
print(n)
R = 8.314
deltaQ = - snitt_dm * L / 1000
T0 = T0r
def epsilon(y):
    return y/(math.exp(y) - 1)

def deltaqfunk(theta):
    return 3 * n * R * (T0*epsilon(theta/T0) - Tf*epsilon(theta/Tf)) + deltaQ

T0 = T0r + 3
oe_t0p = fsolve(deltaqfunk, 283)
T0 = T0r - 3
oe_t0m = fsolve(deltaqfunk, 283)

T0 = T0r
deltaQ = - dm1 * L / 1000
oe_dm1 = fsolve(deltaqfunk, 283)
deltaQ = - dm2 * L / 1000
oe_dm2 = fsolve(deltaqfunk, 283)

deltaQ = - snitt_dm * L / 1000
n = (5.997 + 0.05) / 26.98
oe_np = fsolve(deltaqfunk, 283)
n = (5.997 - 0.05) / 26.98
oe_nm = fsolve(deltaqfunk, 283)

dmg = 0.5 * (oe_dm1 - oe_dm2)
t0g = 0.5 * (oe_t0p - oe_t0m)
ng = 0.5 * (oe_np - oe_nm)

print("Massesensitivitet: {0}".format(dmg))
print("Temperatursensitivitet: {0}".format(t0g))
print("Prøvesensitivitet: {0}".format(ng))

gauss = math.sqrt(dmg**2 + t0g**2 + ng**2)
print("Gauss: {0}".format(gauss))