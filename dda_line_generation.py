import math
import matplotlib.pyplot as plt


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('DDA Line generating algorithm')
    plt.show()


def plot_line(x1: int, y1: int, x2: int, y2: int):
    # Always keep x2 to the right of x1.
    if (x2 < x1):
        x2, x1 = x1, x2
        y2, y1 = y1, y2

    dx = x2 - x1
    dy = y2 - y1

    # Slope
    m = dy / dx
    x = x1
    y = y1

    x_pts = [x1]
    y_pts = [y1]

    # y = y1 + (x - x1) * m
    # x = x1 + (y - y1) / m
    while (x < x2):
        if (abs(m) < 1):
            x += 1
            y = y1 + (x - x1) * m
            # y = math.floor(y)
        else:
            y += 1
            x = x1 + (y - y1) / m
            # x = math.floor(x)
        x_pts.append(x)
        y_pts.append(y)

    plot(x_pts, y_pts)


def plot_line_steps(x1: int, y1: int, x2: int, y2: int):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x_pts = [x1]
    y_pts = [y1]

    x = x1
    y = y1
    for _ in range(steps):
        x += x_inc
        y += y_inc
        x_pts.append(x)
        y_pts.append(y)

    plot(x_pts, y_pts)


x1 = int(input('Enter x1:  '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

# plot_line(x1, y1, x2, y2)
plot_line_steps(x1, y1, x2, y2)
