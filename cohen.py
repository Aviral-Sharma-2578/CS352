import numpy as np 
import matplotlib.pyplot as plt

TOP = 8
BOTTOM = 4
LEFT = 1
RIGHT = 2

x_min = 10 
x_max = 30
y_min = 10
y_max = 30

def compute_code(x, y):
  code = 0
  if x < x_min:
    code = code | LEFT
  if x > x_max:
    code = code | RIGHT
  if y < y_min:
    code = code | BOTTOM
  if y > y_max:
    code = code | TOP
  return code

x0, y0 = 4, 6
x1, y1 = 34, 36

plt.plot([x0, x1], [y0, y1],"r.--")
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color="g")

while True:
  x_new, y_new = x0, y0

  code0 = compute_code(x0, y0)
  code1 = compute_code(x1, y1)

  if code0 == 0 and code1 == 0:
    break
    
  if code0 & code1:
    break

  code_out = code0 if code0 else code1

  if code_out & TOP:
    y_new = y_max
    x_new = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
  if code_out & BOTTOM:
    y_new = y_min
    x_new = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
  if code_out & RIGHT:
    x_new = x_max
    y_new = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
  if code_out & LEFT:
    x_new = x_min
    y_new = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)

  if code_out == code0:
    x0, y0 = x_new, y_new
  else:
    x1, y1 = x_new, y_new

print(x0, y0)
print(x1, y1)

plt.plot([x0, x1], [y0, y1])

plt.show()