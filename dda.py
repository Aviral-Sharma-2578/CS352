import matplotlib.pyplot as plt


def dda_line(x0, y0, x1, y1):
    points = []

    dx = x1 - x0
    dy = y1 - y0

    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x0, y0
    for _ in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points


def plot_line(points):
    x_vals, y_vals = zip(*points)
    plt.plot(x_vals, y_vals, marker='o', color='green', linestyle='None')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("DDA Line Drawing Algorithm")
    plt.grid(True)
    plt.show()


# Example input
x_start, y_start = 2, 3
x_end, y_end = 10, 7

points = dda_line(x_start, y_start, x_end, y_end)
print("Generated points:", points)
plot_line(points)
