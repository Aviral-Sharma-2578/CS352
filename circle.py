import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x, y = 0, r
    p = 1 - r  # Initial decision parameter
    points = []

    def plot_circle_points(xc, yc, x, y):
        # Using symmetry to plot all 8 points
        points.extend([
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ])

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

    return points

# Plotting the circle
xc, yc, r = 0, 0, 10  # Circle center (0,0) and radius 10
circle_points = midpoint_circle(xc, yc, r)

# Extracting x and y coordinates
x_vals, y_vals = zip(*circle_points)
plt.scatter(x_vals, y_vals, s=10, color='red')
plt.gca().set_aspect('equal')
plt.title("Midpoint Circle Algorithm")
plt.show()
