import matplotlib.pyplot as plt


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Ellipse drawing algorithm')
    plt.show()


def plot_ellipse(rx: int, ry: int):
    dirs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    x_pts = []
    y_pts = []

    # Initial
    # Start at top of the ellipse
    x = 0
    y = ry
    # Initial decision parameter for region 1
    p1 = ry * ry + (1/4) * rx * rx - ry * rx * rx

    # Plot region 1
    while (x * ry * ry < y * rx * rx):
        for dx, dy in dirs:
            x_pts.append(x * dx)
            y_pts.append(y * dy)

        if (p1 < 0):
            # mid point is inside the ellipse
            x += 1
            p1 += 2 * ry * ry * x + ry*ry
        else:
            # mid point is outside the ellipse
            x += 1
            y -= 1
            p1 += 2 * ry * ry * x - 2*rx*rx*y + ry*ry

    # Initial decision parameter for region 2
    p2 = (x + 0.5) * (x + 0.5) * ry * ry + (y-1) * (y-1) * rx*rx - rx*rx*ry*ry

    # Plot region 2
    while (y >= 0):
        for dx, dy in dirs:
            x_pts.append(x * dx)
            y_pts.append(y * dy)

        if (p2 > 0):
            y -= 1
            p2 += rx*rx - 2*y*rx*rx
        else:
            y -= 1
            x += 1
            p2 += 2*ry*ry*x - 2*rx*rx*y + rx*rx

    plot(x_pts, y_pts)


rx = int(input("enter rx: "))
ry = int(input("enter ry: "))

plot_ellipse(rx, ry)
