import numpy as np
import matplotlib.pyplot as plt

# Define the original point
orig_pt = np.array([6, 3])

# Translation vector (-2, 4)
trans_vec = np.array([-2, 4])

# Perform translation
new_pt = orig_pt + trans_vec

# Plot the original and translated points
plt.figure()
plt.scatter(*orig_pt, color='blue', label='Initial (6,3)')
plt.scatter(*new_pt, color='red', label='After Translation')

# Draw a dashed line connecting the points
plt.plot([orig_pt[0], new_pt[0]], [orig_pt[1], new_pt[1]], 'g--')

# Labels, grid, and title
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.title("2D Point Translation")
plt.axis('equal')  # Optional for proper aspect ratio
plt.show()
