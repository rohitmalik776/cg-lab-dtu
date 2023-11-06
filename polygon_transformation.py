import math
import matplotlib.pyplot as plt


def plot(x: list, y: list, x_new: list, y_new: list):
    plt.scatter(x, y, c='red')
    plt.scatter(x_new, y_new, c='blue')
    plt.legend(['old point', 'new point'])

    plt.axhline(0, c='gray')
    plt.axvline(0, c='gray')

    max_val = max(x + y + x_new + y_new) + 1
    min_val = min(x + y + x_new + y_new) - 1
    min_val = min(min_val, 0)

    plt.ylim((min_val, max_val))
    plt.xlim((min_val, max_val))
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Point Transformation')
    plt.show()


def plot_line(x1: int, y1: int, x2: int, y2: int):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
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

    return x_pts, y_pts


def draw_polygon(x_old: list, y_old: list, x_new: list, y_new: list, n: int, ref=False):
    new_x_pts = []
    new_y_pts = []

    old_x_pts = []
    old_y_pts = []

    for i in range(n):
        if (ref):
            if (i+1 >= n):
                break
        x, y = plot_line(x_new[i], y_new[i], x_new[i+1], y_new[i+1])
        new_x_pts = new_x_pts + x
        new_y_pts = new_y_pts + y

        x, y = plot_line(x_old[i], y_old[i], x_old[i+1], y_old[i+1])
        old_x_pts = old_x_pts + x
        old_y_pts = old_y_pts + y

    plot(old_x_pts, old_y_pts, new_x_pts, new_y_pts)


def translate(x: list, y: list, tx: int, ty: int, n: int):
    x_new = [i + tx for i in x]
    y_new = [j + ty for j in y]
    draw_polygon(x, y, x_new, y_new, n)


def scale(x: list, y: list, sx: float, sy: float):
    x_new = [i * sx for i in x]
    y_new = [j * sy for j in y]
    draw_polygon(x, y, x_new, y_new, n)


def rotate(x: list, y: list, angle: float):
    n = len(x)
    x_new = [x[i] * math.cos(angle) - y[i] * math.sin(angle) for i in range(n)]
    y_new = [x[i] * math.sin(angle) + y[i] * math.cos(angle) for i in range(n)]
    draw_polygon(x, y, x_new, y_new, n, True)


def reflect(x: list, y: list, is_x: bool):
    n = len(x)
    x_new = [x[i] * (1 if is_x else -1) for i in range(n)]
    y_new = [y[i] * (-1 if is_x else 1) for i in range(n)]
    draw_polygon(x, y, x_new, y_new, n, True)


n = int(input('Enter number of vertices: '))
x = []
y = []
for _ in range(n):
    x_pt = int(input('Enter x: '))
    y_pt = int(input('Enter y: '))
    x.append(x_pt)
    y.append(y_pt)

x.append(x[0])
y.append(y[0])


print('1. Translation\n2. Scaling\n3. Rotation\n4. Reflection')
choice = int(input('Enter a choice: '))

assert (choice >= 1 and choice <= 4)

if choice == 1:
    tx = int(input('Enter tx: '))
    ty = int(input('Enter ty: '))
    translate(x, y, tx, ty, n)
elif choice == 2:
    sx = float(input('Enter sx: '))
    sy = float(input('Enter sy: '))
    scale(x, y, sx, sy)
elif choice == 3:
    angle = int(input('Enter theta in degrees: '))
    angle = (angle * math.pi) / 180
    rotate(x, y, angle)
else:
    about_x = int(
        input("0: reflection about y-axis\n1: reflection about x-axis\nEnter choice:")
    )
    is_x = about_x == 1
    reflect(x, y, is_x)
