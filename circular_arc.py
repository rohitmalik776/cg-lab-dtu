import matplotlib.pyplot as plt
import math


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.ylim((-50, 50))
    plt.xlim((-50, 50))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Circular arc drawing algorithm')
    plt.show()


def plot_circular_arc(r: int, sa: int, ea: int):
    sa = (sa * math.pi) / 180
    ea = (ea * math.pi) / 180

    x_pts = []
    y_pts = []

    theta = sa

    while (theta <= ea):
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        theta += 0.01
        x_pts.append(x)
        y_pts.append(y)

    plot(x_pts, y_pts)


r = int(input('Enter radius: '))
sa = int(input('Enter start angle: '))
ea = int(input('Enter end angle: '))

plot_circular_arc(r, sa, ea)
