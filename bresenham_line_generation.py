import math
import matplotlib.pyplot as plt


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Bresenham Line generating algorithm')
    plt.show()


def plot_line(x1: int, y1: int, x2: int, y2: int):
    # Always keep x2 to the right of x1.
    if (x2 < x1):
        x2, x1 = x1, x2
        y2, y1 = y1, y2

    dx = x2 - x1
    dy = y2 - y1

    p = 2 * dy - dx
    x = x1
    y = y1

    x_pts = [x]
    y_pts = [y]

    while (x <= x2):
        if (p < 0):
            p = p + 2 * dy
        else:
            p = p + 2 * dy - 2 * dx
            y += 1
        x += 1
        x_pts.append(x)
        y_pts.append(y)

    plot(x_pts, y_pts)


x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

plot_line(x1, y1, x2, y2)
