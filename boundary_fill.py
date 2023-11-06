from matplotlib import pyplot
import time
import numpy as np


def gen_boundary(width: int, height: int, matrix: list[list[str]], b: str):
    x, y = 0, 0
    while (x < width):
        matrix[x][y] = b
        x += 1
    x -= 1
    while (y < height):
        matrix[x][y] = b
        y += 1
    y -= 1
    while (x >= 0):
        matrix[x][y] = b
        x -= 1
    x += 1
    while (y >= 0):
        matrix[x][y] = b
        y -= 1
    y += 1


def boundary_fill(matrix: list[list[str]], x: int, y: int, c: str, b: str, fig, ax):
    if (matrix[x][y] == c or matrix[x][y] == b):
        return

    matrix[x][y] = c
    ax.scatter([x], [y], color=matrix[x][y])
    fig.canvas.flush_events()
    # time.sleep(0.1)

    dirs = [[0, 1], [0, -1], [-1, 0], [1, 0],
            [-1, -1], [-1, 1], [1, -1], [1, 1]]

    for i in range(len(dirs)):
        boundary_fill(matrix, x+dirs[i][0], y + dirs[i][1], c, b, fig, ax)


GRAPH_SIZE = 10
BOUNDARY_COLOR = 'red'
FILL_COLOR = 'green'
DEFAULT_COLOR = 'white'

matrix = [[DEFAULT_COLOR] * GRAPH_SIZE for i in range(GRAPH_SIZE)]
gen_boundary(GRAPH_SIZE, GRAPH_SIZE, matrix, BOUNDARY_COLOR)

pyplot.ion()

fig, ax = pyplot.subplots()

for i in range(0, GRAPH_SIZE):
    for j in range(0, GRAPH_SIZE):
        ax.scatter([i], [j], color=matrix[i][j])


boundary_fill(matrix, GRAPH_SIZE//2, GRAPH_SIZE//2,
              FILL_COLOR, BOUNDARY_COLOR, fig, ax)

time.sleep(5)
