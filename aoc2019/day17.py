from io import StringIO
from aocd import data
from intcode import *
from utils import *

robot = Intcode(data)
o = StringIO()
robot.ascii(out=o)
grid = {}

directions = {
    'v': Point(0, 1),
    '^': Point(0, -1),
    '<': Point(-1, 0),
    '>': Point(1, 0),
}
pos, facing = None, None

for y, row in enumerate(o.getvalue().strip().splitlines()):
    for x, val in enumerate(row):
        pt = Point(x, y)
        grid[pt] = val
        if val in directions:
            pos, facing = pt, directions[val]
assert pos is not None and facing is not None
print(
    sum(p.x * p.y for p, v in grid.items() if v == '#' and all(
        grid.get(p + d) == '#' for d in directions.values())))

path = []
while True:
    if grid.get(pos + facing.ccw()) == '#':
        path.append('L')
        facing = facing.ccw()
    elif grid.get(pos + facing.cw()) == '#':
        path.append('R')
        facing = facing.cw()
    else:
        break
    n = 0
    while grid.get(pos + facing) == '#':
        n += 1
        pos += facing
    path.append(n)
path = ','.join(map(str, path))

maxlen = 20


def simplify(path: str, char: str) -> str:
    lst = path.split(',')
    routines = set()
    for i in range(0, len(lst)):
        if lst[i] not in 'LR':
            continue
        for j in range(i + 1, len(lst)):
            if lst[j] in 'LR':
                continue
            if not lst[j].isnumeric():
                break
            routine = ','.join(lst[i:j + 1])
            if len(routine) > maxlen:
                break
            routines.add(routine)
    return min(routines, key=lambda r: len(path.replace(r, char)))


routines = []
for char in 'ABC':
    r = simplify(path, char)
    routines.append(r)
    path = path.replace(r, char)

lines = [path, *routines, 'n']
i = StringIO('\n'.join(lines))
robot = Intcode(data)
robot[0] = 2
print(robot.ascii(i, StringIO()))
