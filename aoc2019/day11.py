from aocd import data
from intcode import *
from utils import *

BLACK = 0
WHITE = 1

LEFT = 0
RIGHT = 1


def run(grid, starting_color=BLACK):
    robot = Intcode(data)
    pos = Point(0, 0)
    grid[pos] = starting_color
    facing = Point(0, -1)
    while True:
        robot.write(grid.get(pos, BLACK))
        out = robot.read(2)
        if len(out) != 2:
            break
        color, direction = out
        grid[pos] = color
        if direction == LEFT:
            facing = facing.ccw()
        else:
            facing = facing.cw()
        pos += facing


grid = {}
run(grid)
print(len(grid))

grid.clear()
run(grid, WHITE)
g = {p: '#' for p, v in grid.items() if v == WHITE}
print(grid_string(g))