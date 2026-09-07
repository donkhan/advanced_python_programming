import matplotlib.pyplot as plt

# Range of complex numbers
xmin, xmax = -2, 1
ymin, ymax = -1.5, 1.5

points = 20          # 20 x 20 grid
max_iter = 20

x_values = []
y_values = []
colors = []

for i in range(points):
    x = xmin + (xmax - xmin) * i / (points - 1)
    for j in range(points):
        y = ymin + (ymax - ymin) * j / (points - 1)
        c = complex(x, y)
        z = 0
        iteration = 0
        while abs(z) <= 2 and iteration < max_iter:
            z = z*z + c
            iteration += 1
        x_values.append(x)
        y_values.append(y)
        colors.append(iteration)
        print(x,y,iteration)

plt.figure(figsize=(6,6),label="Mandelbrot")
plt.scatter(x_values, y_values, c=colors, cmap="viridis", s=80)
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.title("Simple Mandelbrot ")
plt.colorbar(label="Iterations before Escape")
plt.show()