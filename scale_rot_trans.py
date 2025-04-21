import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Original point in homogeneous coordinates
point = np.array([6, 2, 7, 1])

# 1. Define Transformation Matrices

# Scaling matrix
scale_mat = np.array([
    [2.0, 0,   0,   0],
    [0,   0.5, 0,   0],
    [0,   0,   1.5, 0],
    [0,   0,   0,   1]
])

# Rotation matrix (60° about the Z-axis)
theta = np.radians(60)
rot_mat = np.array([
    [np.cos(theta), -np.sin(theta), 0, 0],
    [np.sin(theta),  np.cos(theta), 0, 0],
    [0,              0,             1, 0],
    [0,              0,             0, 1]
])

# Translation matrix
trans_mat = np.array([
    [1, 0, 0,  4],
    [0, 1, 0, -3],
    [0, 0, 1,  5],
    [0, 0, 0,  1]
])

# 2. Composite transformation: T * R * S
composite_mat = trans_mat @ rot_mat @ scale_mat

# 3. Apply transformations step-by-step
scaled_pt = scale_mat @ point
rotated_pt = rot_mat @ scaled_pt
transformed_pt = trans_mat @ rotated_pt

print("Original Point:", point)
print("After Scaling:", scaled_pt)
print("After Rotation:", rotated_pt)
print("After Translation (Final Point):", transformed_pt)

# 4. Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract coordinates for plotting
pts = np.array([point, scaled_pt, rotated_pt, transformed_pt])
colors = ['blue', 'orange', 'purple', 'red']
labels = ['Original', 'Scaled', 'Rotated', 'Transformed']

# Plot points
for i in range(4):
    ax.scatter(*pts[i][:3], color=colors[i], label=labels[i])
    ax.plot([0, pts[i][0]], [0, pts[i][1]], [0, pts[i][2]], color=colors[i], linestyle='dashed')

# Settings
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Transformations (Scaling → Rotation → Translation)")
ax.legend()
plt.show()
