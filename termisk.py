import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(0.01, 0.99, 1000)
y = np.linspace(0.01, 0.99, 1000)
for i in x:
    for j in y:
        if ((2 * i * j - i - 1) / (j ** 2 + i * j ** 2 - 2 * j) <= 1):
            print("VALUE UNDER ONE! {} {}".format(i, j))
x, y = np.meshgrid(x, y)
z = (2 * x * y - x - 1) / (y ** 2 + x * y ** 2 - 2 * y)

surface = ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=True, vmin=0, vmax=6)
ax.set_zlim(0, 6)
ax.set_xlabel(r"$(H_2/H_1)^2$")
ax.set_ylabel(r"$(T_1/T_2)$")
plt.show()