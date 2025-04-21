import numpy as np
import matplotlib.pyplot as plt

# Generate values for x-axis (0 to 2π)
x_vals = np.linspace(0, 2 * np.pi, 100)  # 100 evenly spaced points

# Compute sine and cosine values
sin_vals = np.sin(x_vals)
cos_vals = np.cos(x_vals)

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot sine curve
plt.plot(x_vals, sin_vals, marker='o', linestyle='-', color='blue', label='Sine Function')

# Plot cosine curve
plt.plot(x_vals, cos_vals, marker='x', linestyle='--', color='red', label='Cosine Function')

# Add labels and title
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph of Sine and Cosine Waves')

# Enable legend and grid
plt.legend()
plt.grid(True)

# Display the plot
plt.show()
