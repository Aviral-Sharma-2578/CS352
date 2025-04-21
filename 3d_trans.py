import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Define the original point in homogeneous coordinates
orig_pt = np.array([4, 2, 7, 1])
# 4x4 Translation Matrix (shifting X by +3, Y by -2, Z by +5)
trans_mat = np.array([[1, 0, 0, 3],
 [0, 1, 0, -2],
 [0, 0, 1, 5],
 [0, 0, 0, 1]])
# Perform translation
new_pt = trans_mat @ orig_pt
# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*orig_pt[:3], color='blue', label='Initial')
ax.scatter(*new_pt[:3], color='red', label='Translated')
# Labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Point Translation")
ax.legend()
plt.show()
