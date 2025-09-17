import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 1, 50)
r_grid, theta_grid = np.meshgrid(r, theta)
z = np.sin(5 * theta_grid) * r_grid

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
c = ax.pcolormesh(theta, r, z.T, cmap='plasma')
fig.colorbar(c, label='Intensity')
plt.title("Polar Heatmap")
plt.show()
