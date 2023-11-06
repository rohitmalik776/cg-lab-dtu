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


def translate(x: int, y: int, tx: int, ty: int):
    x_new = [x + tx]
    y_new = [y + ty]
    plot([x], [y], x_new, y_new)


def scale(x: int, y: int, sx: float, sy: float):
    x_new = [x * sx]
    y_new = [y * sy]
    plot([x], [y], x_new, y_new)


def rotate(x: int, y: int, angle: float):
    x_new = [x * math.cos(angle) - y * math.sin(angle)]
    y_new = [x * math.sin(angle) + y * math.cos(angle)]
    plot([x], [y], x_new, y_new)


x = int(input('Enter x: '))
y = int(input('Enter y: '))

print('1. Translation\n2. Scaling\n3. Rotation')
choice = int(input('Enter a choice: '))

assert (choice >= 1 and choice <= 3)

if choice == 1:
    tx = int(input('Enter tx: '))
    ty = int(input('Enter ty: '))
    translate(x, y, tx, ty)
elif choice == 2:
    sx = float(input('Enter sx: '))
    sy = float(input('Enter sy: '))
    scale(x, y, sx, sy)
else:
    angle = int(input('Enter theta in degrees: '))
    angle = (angle * math.pi) / 180
    rotate(x, y, angle)
