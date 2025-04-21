import numpy as np
import matplotlib.pyplot as plt

# Define the initial point
original_point = np.array([5, 2])

# Shear transformation matrix (0.7 in X-direction, 0.3 in Y-direction)
shear_mat = np.array([
    [1, 0.7],
    [0.3, 1]
])

# Apply shear transformation
transformed_point = shear_mat @ original_point

# Plotting
plt.figure()
plt.scatter(*original_point, color='blue', label='Original (5,2)')
plt.scatter(*transformed_point, color='red', label='Sheared')

# Draw lines connecting the origin
plt.plot([0, original_point[0]], [0, original_point[1]], 'b--')
plt.plot([0, transformed_point[0]], [0, transformed_point[1]], 'r--')

# Labels and display
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.title("Shear Transformation in 2D")
plt.axis('equal')  # Optional for consistent scaling
plt.show()
