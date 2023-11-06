import matplotlib.pyplot as plt
import math


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.ylim((-50, 50))
    plt.xlim((-50, 50))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Elliptical arc drawing algorithm')
    plt.show()


def plot_elliptical_arc(rx: int, ry: int, sa: int, ea: int):
    sa = (sa * math.pi) / 180
    ea = (ea * math.pi) / 180

    x_pts = []
    y_pts = []

    theta = sa

    while (theta <= ea):
        x = rx * math.cos(theta)
        y = ry * math.sin(theta)
        theta += 0.01
        x_pts.append(x)
        y_pts.append(y)

    plot(x_pts, y_pts)


rx = int(input('Enter rx: '))
ry = int(input('Enter ry: '))
sa = int(input('Enter start angle: '))
ea = int(input('Enter end angle: '))

plot_elliptical_arc(rx, ry, sa, ea)
