import numpy as np
import matplotlib.pyplot as plt

theta1 = np.radians(40)
theta2 = np.radians(60)
theta3 = theta1 + theta2

point = np.array([5, 3, 7, 1])

def rotate(theta):
  return np.array([[np.cos(theta), -np.sin(theta), 0, 0], [np.sin(theta), np.cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

R1 = rotate(theta1)
R2 = rotate(theta2)
R3 = rotate(theta3)

P1 = R2 @ R1 @ point
P2 = R3 @ point

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*point[:3], label='original point')
ax.scatter(*P1[:3], 'g', label='point1')
ax.scatter(*P2[:3], 'r', marker='x', label='point2')
plt.grid(True)
plt.legend()

plt.show()