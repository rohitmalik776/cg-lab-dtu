import matplotlib.pyplot as plt
import math


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.xlim((0, 80))
    plt.ylim((0, 80))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Thick Line generating algorithm')
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

    return x_pts, y_pts


def draw_thick_line(x1: int, y1: int, x2: int, y2: int, w: int):
    x_pts = []
    y_pts = []
    x_main, y_main = plot_line(x1, y1, x2, y2)
    x_pts = x_pts + x_main
    y_pts = y_pts + y_main

    hyp = math.sqrt((y2-y1)**2 + (x2-x1) ** 2)
    wy = ((w-1) * hyp) / (2 * abs(x2-x1))
    wy = int(wy)

    for i in range(1, wy+1, 1):
        x_cur, y_cur = plot_line(x1, y1 + i, x2, y2 + i)
        x_pts = x_pts + x_cur
        y_pts = y_pts + y_cur
    for i in range(1, wy+1, 1):
        x_cur, y_cur = plot_line(x1, y1 - i, x2, y2 - i)
        x_pts = x_pts + x_cur
        y_pts = y_pts + y_cur

    plot(x_pts, y_pts)


x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
w = int(input("thickness: "))

draw_thick_line(x1, y1, x2, y2, w)
