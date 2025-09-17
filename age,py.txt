import matplotlib.pyplot as plt

# Data
age_groups = ['0–14', '15–24', '25–44', '45–64', '65+']
population = [15000, 12000, 25000, 20000, 10000]

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(age_groups, population, color='skyblue', edgecolor='black')

# Add labels and title
plt.title('Population Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Population')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
