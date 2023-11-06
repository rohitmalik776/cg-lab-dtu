import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class Window:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

        self.width = max_x - min_x
        self.height = max_y - min_y

        self.CENTER = 0
        self.LEFT = 1
        self.RIGHT = 2
        self.BOTTOM = 4
        self.TOP = 8

    def __str__(self):
        return f'min x: {self.min_x}\nmin y: {self.min_y}\nmax x: {self.max_x}\nmax y: {self.max_y}'

    def get_code(self, x: int, y: int) -> int:
        # Code format = TBRL
        code = 0
        if (x < self.min_x):
            code = code | self.LEFT
        if (x > self.max_x):
            code = code | self.RIGHT
        if (y < self.min_y):
            code = code | self.BOTTOM
        if (y > self.max_y):
            code = code | self.TOP
        return code

    def clip_point(self, x: int, y: int, m: float, code: int):
        while (code != 0):
            if ((code & self.TOP) != 0):
                y_clip = self.max_y
                x_clip = ((y_clip - y) / m) + x
                x = x_clip
                y = y_clip

            if ((code & self.BOTTOM) != 0):
                y_clip = self.min_y
                x_clip = ((y_clip - y) / m) + x
                x = x_clip
                y = y_clip

            if ((code & self.LEFT) != 0):
                x_clip = self.min_x
                y_clip = m * (x_clip - x) + y
                x = x_clip
                y = y_clip

            if ((code & self.RIGHT) != 0):
                x_clip = self.max_x
                y_clip = m * (x_clip - x) + y
                x = x_clip
                y = y_clip

            code = self.get_code(x, y)

        return x, y

    def cohen_clip(self, x1: int, y1: int, x2: int, y2: int):
        # Step 1: Find the codes for end points.
        code1 = self.get_code(x1, y1)
        code2 = self.get_code(x2, y2)

        # Step 2: Find out if both the points lie inside the viewport
        if ((code1 | code2) == 0):
            print("No clipping whatsoever")
            return x1, y1, x2, y2

        # Step 3: Perform and operation on codes
        if (code1 & code2 != 0):
            print("Line is completely outside")
            return 0, 0, 0, 0

        print("Line is partially visible")

        # Step 4: Clip the line
        m = (y2-y1) / (x2-x1)

        # First, clip (x1, y1)
        x1, y1 = self.clip_point(x1, y1, m, code1)

        # Clip (x2, y2)
        x2, y2 = self.clip_point(x2, y2, m, code2)

        return x1, y1, x2, y2

    def liang_clip(self, x1: int, y1: int, x2: int, y2: int):
        dx = x2 - x1
        dy = y2 - y1

        p = [-dx, dx, -dy, dy]
        q = [x1 - self.min_x, self.max_x - x1,
             y1 - self.min_y, self.max_y - y1]

        for i in range(len(p)):
            if (p[i] == 0):
                if (q[i] < 0):
                    print("Line is completely outside")
                    return 0, 0, 0, 0

        t1 = 0
        t2 = 1
        for i in range(len(p)):
            if (p[i] < 0):
                t1 = max(t1, q[i] / p[i])
            if (p[i] > 0):
                t2 = min(t2, q[i] / p[i])

        if (t1 < t2):
            f_x1 = x1 + t1 * dx
            f_y1 = y1 + t1 * dy
            f_x2 = x1 + t2 * dx
            f_y2 = y1 + t2 * dy
            return f_x1, f_y1, f_x2, f_y2
        else:
            print("Line is outside")
            return 0, 0, 0, 0


def test(test_cohen=True):
    fig, ax = plt.subplots()
    plt.xlim((0, 20))
    plt.ylim((0, 20))

    ax.add_patch(Rectangle((window.min_x, window.min_y), window.width,
                           window.height, edgecolor='gray', fill=False))

    lines = [
        [1, 0, 11, 15],
        [0, 8, 5, 12],
        [7, 0, 11, 5],
        [3, 5, 8, 5],
        [3, 1, 8, 1],
        [12, 2, 12, 8],
        [1, 2, 1, 8],
        [0, 5, 5, 0],
        [0, 15, 15, 0],
        [0, 13, 13, 0],
        [0, 12, 14, 12],
        [0, 6, 15, 6],
    ]

    for i in range(len(lines)):
        x1 = lines[i][0]
        y1 = lines[i][1]
        x2 = lines[i][2]
        y2 = lines[i][3]
        if (test_cohen):
            nx1, ny1, nx2, ny2 = window.cohen_clip(x1=x1, y1=y1, x2=x2, y2=y2)
        else:
            nx1, ny1, nx2, ny2 = window.liang_clip(x1=x1, y1=y1, x2=x2, y2=y2)

        ax.plot([x1, x2], [y1, y2], color='red')
        ax.plot([nx1, nx2], [ny1, ny2], color='blue')

    plt.legend(['Viewport', 'Original line', 'Clipped line'])

    plt.show()


window = Window(min_x=2, max_x=10, min_y=2, max_y=10)
print(window)

test(test_cohen=True)
