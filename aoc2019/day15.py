from copy import deepcopy
from typing import Iterable
from aocd import data
from intcode import *
from utils import *

directions = {
    1: Point(0, -1),
    2: Point(0, 1),
    3: Point(-1, 0),
    4: Point(1, 0),
}

WALL = 0
MOVED = 1
OXYGEN = 2


class Droid(Intcode):

    def __init__(self, data: str) -> None:
        super().__init__(data)
        self.pos = Point(0, 0)

    def go(self, d):
        self.write(d)
        status, = self.read(1)
        if status != WALL:
            self.pos += directions[d]
        return status


MAP = {}
DROIDS = {Point(0, 0): Droid(data)}


def successors(p: Point) -> Iterable[Point]:
    d = DROIDS[p]
    for k, v in directions.items():
        p_ = p + v
        if p_ not in MAP:
            d_ = deepcopy(d)
            s = d_.go(k)
            MAP[p_] = s
            if s != WALL:
                DROIDS[p_] = d_
                yield p_


prev, _ = bfs(Point(0, 0), successors, lambda p: MAP.get(p) == OXYGEN)
path = [next(k for k, v in MAP.items() if v == OXYGEN)]
while True:
    x = prev[path[-1]]
    if x is None:
        break
    path.append(x)
print(len(path) - 1)

MAP.clear()
_, dist = bfs(path[0], successors, lambda _: False)
print(max(dist.values()))