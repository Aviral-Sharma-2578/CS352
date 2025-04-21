import numpy as np
import matplotlib.pyplot as plt

a = 40
b = 20
x = 0
y = -b
p = -b

cx, cy = 50, 50
grid = np.zeros((100, 100), dtype=np.uint8)

def draw(x, y):
    grid[cx + x, cy + y] = 255
    grid[cx + x, cy - y] = 255
    grid[cx - x, cy + y] = 255
    grid[cx - x, cy - y] = 255

while x*b*b < -y*a*a:
  if p > 0:
    y += 1
    p += 2*x*b*b + 2*y*a*a + b*b
  else:
    p += 2*x*b*b + b*b
  draw(x, y)
  x += 1

while -y > 0:
  if p < 0:
    x += 1
    p += 2*x*b*b + 2*y*a*a + a*a
  else:
    p += 2*y*a*a + a*a
  draw(x, y)
  y += 1

plt.imshow(grid, cmap='gray')
plt.axis('off')
plt.show()