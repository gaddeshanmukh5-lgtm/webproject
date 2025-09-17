import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6]
rainfall = [78, 60, 85, 70, 55, 40, 35, 38, 50, 65, 80, 90]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(months, temperature, color='red', marker='o', linewidth=2)
ax1.set_title('Average Monthly Temperature (°C)', fontsize=14)
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

for i, temp in enumerate(temperature):
    ax1.text(i, temp + 0.5, f"{temp}°", ha='center', fontsize=9)

ax2.scatter(months, rainfall, color='blue', s=100, edgecolors='black')
ax2.set_title('Average Monthly Rainfall (mm)', fontsize=14)
ax2.set_ylabel('Rainfall (mm)')
ax2.grid(True)

for i, rain in enumerate(rainfall):
    ax2.text(i, rain + 2, f"{rain}mm", ha='center', fontsize=9)

plt.tight_layout()
plt.suptitle('Weather Statistics (2024)', fontsize=16, fontweight='bold', y=1.02)
plt.show()
