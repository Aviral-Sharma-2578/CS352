import numpy as np
import matplotlib.pyplot as plt

# Function to rotate a point around the origin
def rotate_around_origin(point, angle_deg):
    angle_rad = np.radians(angle_deg)
    x_new = point[0] * np.cos(angle_rad) - point[1] * np.sin(angle_rad)
    y_new = point[0] * np.sin(angle_rad) + point[1] * np.cos(angle_rad)
    return (x_new, y_new)

# Function to rotate a point around another point
def rotate_around_point(point, pivot, angle_deg):
    px, py = point[0] - pivot[0], point[1] - pivot[1]
    px, py = rotate_around_origin((px, py), angle_deg)
    return (px + pivot[0], py + pivot[1])

# Function to translate a point
def translate_point(point, dx, dy):
    return (point[0] + dx, point[1] + dy)

# Get user input
num_vertices = int(input("Enter the number of vertices in the polygon: "))

polygon_vertices = []
print("Enter the coordinates (x y) for each vertex:")

for _ in range(num_vertices):
    x, y = map(float, input().split())
    polygon_vertices.append((x, y))

polygon_vertices.append(polygon_vertices[0])  # Close the polygon

# Rotation around origin
rotation_angle_origin = float(input("Enter the angle to rotate around the origin (degrees): "))
rotated_origin = [rotate_around_origin(p, rotation_angle_origin) for p in polygon_vertices]

# Rotation around a given point
pivot_x, pivot_y = map(float, input("Enter the pivot point (x y) for rotation: ").split())
rotation_angle_pivot = float(input("Enter the angle to rotate around the pivot point (degrees): "))
rotated_pivot = [rotate_around_point(p, (pivot_x, pivot_y), rotation_angle_pivot) for p in polygon_vertices]

# Translation
dx, dy = map(float, input("Enter translation values (dx dy): ").split())
translated_polygon = [translate_point(p, dx, dy) for p in polygon_vertices]

# Function to plot the polygons
def plot_polygon(polygon, title, color):
    x, y = zip(*polygon)
    plt.plot(x, y, marker='o', color=color, label=title)
    plt.fill(x, y, color=color, alpha=0.3)
    plt.legend()

# Plot the results
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plot_polygon(polygon_vertices, "Original Polygon", 'blue')

plt.subplot(1, 4, 2)
plot_polygon(rotated_origin, "Rotated Around Origin", 'green')

plt.subplot(1, 4, 3)
plot_polygon(rotated_pivot, "Rotated Around Pivot", 'purple')

plt.subplot(1, 4, 4)
plot_polygon(translated_polygon, "Translated Polygon", 'red')

plt.tight_layout()
plt.show()
