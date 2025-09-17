import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 6))  # Set figure size

plt.plot(x, y_sin, label='Sine', color='blue', linestyle='--', linewidth=2)

plt.plot(x, y_cos, label='Cosine', color='red', linestyle='-', linewidth=2)

plt.title('Sine and Cosine Waves')
plt.xlabel('Angle [radians]')
plt.ylabel('Value')

plt.legend()

plt.grid(True)

plt.show()
