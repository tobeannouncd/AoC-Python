from collections import defaultdict

from aoc2019.intcode import VM
from lattice import Point, to_str


def solve(data: str) -> None:
    vm = VM(data)

    def paint(hull):
        pos, facing = Point(0, 0), Point(0, -1)
        for _ in vm.reset():
            hull[pos], direction = vm.send(hull[pos]).get(2)
            facing = facing.rot_cw() if direction else facing.rot_ccw()
            pos += facing

    hull = defaultdict(int)
    paint(hull)
    print(len(hull))

    hull.clear()
    hull[Point(0, 0)] = 1
    paint(hull)

    print(to_str(pt for pt, val in hull.items() if val == 1))


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
