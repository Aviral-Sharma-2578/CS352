import numpy as np
import matplotlib.pyplot as plt

grid = np.zeros((100, 100))

def drawPixel(x, y):
  grid[x][y] = 255

def drawLineH(x0, y0, x1, y1):
  if(x0 > x1):
    x0, x1 = x1, x0
    y0, y1 = y1, y0

  dx = x1 - x0
  dy = y1 - y0

  dirs = -1 if dy < 0 else 1
  dy *= dirs

  if dx != 0:
    y = y0
    p = 2*dy - dx
    for i in range(dx + 1):
      drawPixel(x0 + i, y)
      if p >= 0:
        y += dirs
        p = p - 2*dx
      p = p + 2*dy

def drawLineV(x0, y0, x1, y1):
  if(y0 > y1):
    x0, x1 = x1, x0
    y0, y1 = y1, y0

  dx = x1 - x0
  dy = y1 - y0

  dirs = -1 if dx < 0 else 1
  dx *= dirs

  if dy != 0:
    x = x0
    p = 2*dx - dy
    for i in range(dy + 1):
      drawPixel(x, y0 + i)
      if p >= 0:
        x += dirs
        p = p - 2*dy
      p = p + 2*dx

drawLineH(10, 10, 50, 20)
plt.imshow(grid, cmap='gray')
plt.show()