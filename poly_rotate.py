# n = int(input("Enter the number of points: "))
# X = list(map(int,input("Enter the points' x coordinates: ").split()))
# Y = list(map(int,input("Enter the points' y coordinates: ").split()))
n = 3
X = [0, 5, 2]
Y = [0, 0, 3]
theta = np.radians(60)

Z = list(zip(X, Y))
Z = [np.array(x) for x in Z]


R1 = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
rotated_Z = [R1 @ x for x in Z]

print(Z)
print(rotated_Z)

plot_X = [x[0] for x in rotated_Z]
plot_Y = [x[1] for x in rotated_Z]

X.append(X[0])
Y.append(Y[0])

plot_X.append(plot_X[0])
plot_Y.append(plot_Y[0])

plt.figure()
plt.plot(X, Y, color='r')
plt.plot(plot_X, plot_Y, color='b')
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)

plt.show()