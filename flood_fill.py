from matplotlib import pyplot
import time
import numpy as np
import random
from collections import deque


def gen_boundary(width: int, height: int, matrix: list[list[str]], b: list[str]):
    x, y = 0, 0
    n = len(b)
    random.seed(time.time())
    while (x < width):
        matrix[x][y] = b[random.randint(0, n-1)]
        x += 1
    x -= 1
    while (y < height):
        matrix[x][y] = b[random.randint(0, n-1)]
        y += 1
    y -= 1
    while (x >= 0):
        matrix[x][y] = b[random.randint(0, n-1)]
        x -= 1
    x += 1
    while (y >= 0):
        matrix[x][y] = b[random.randint(0, n-1)]
        y -= 1
    y += 1


def flood_fill(matrix: list[list[str]], beg_x: int, beg_y: int, c: str, b: str, fig, ax):

    q = deque()
    q.append([beg_x, beg_y])
    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0],
            [-1, -1], [-1, 1], [1, -1], [1, 1]]

    while (len(q) > 0):
        [x, y] = q.popleft()

        if (matrix[x][y] != b):
            continue

        matrix[x][y] = c
        ax.scatter([x], [y], color=matrix[x][y])
        fig.canvas.flush_events()

        for i in range(len(dirs)):
            q.append([x+dirs[i][0], y + dirs[i][1]])


GRAPH_SIZE = 10
BOUNDARY_COLORS = ['orange', 'pink', 'yellow']
FILL_COLOR = 'green'
DEFAULT_COLOR = 'white'

matrix = [[DEFAULT_COLOR] * GRAPH_SIZE for i in range(GRAPH_SIZE)]

# Outer square
gen_boundary(GRAPH_SIZE, GRAPH_SIZE, matrix, BOUNDARY_COLORS)
# Inner square
gen_boundary(GRAPH_SIZE//2, GRAPH_SIZE//2, matrix, BOUNDARY_COLORS)
matrix[4][4] = DEFAULT_COLOR

pyplot.ion()

fig, ax = pyplot.subplots()

for i in range(0, GRAPH_SIZE):
    for j in range(0, GRAPH_SIZE):
        ax.scatter([i], [j], color=matrix[i][j])

fig.canvas.flush_events()

flood_fill(matrix, GRAPH_SIZE//4, GRAPH_SIZE//4,
           FILL_COLOR, DEFAULT_COLOR, fig, ax)

time.sleep(5)
