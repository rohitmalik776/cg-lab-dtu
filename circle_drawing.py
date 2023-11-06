import matplotlib.pyplot as plt


def plot(x: list, y: list):
    plt.scatter(x, y)
    plt.xlim((-50, 50))
    plt.ylim((-50, 50))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Mid point circle drawing algorithm')
    plt.show()


def plot_circle(r: int):
    x = 0
    y = r
    p = 1-r

    dirs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

    x_pts = [x]
    y_pts = [y]

    while (x <= y):
        if (p < 0):
            p += 2 * x + 3
        else:
            p += 2 * x - 2 * y + 5
            y -= 1
        x += 1

        for dx, dy in dirs:
            x_pts.append(x * dx)
            y_pts.append(y * dy)

            x_pts.append(y * dx)
            y_pts.append(x * dy)

    plot(x_pts, y_pts)


r = int(input('Enter radius: '))

plot_circle(r)
