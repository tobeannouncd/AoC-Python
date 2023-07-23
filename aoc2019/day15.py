from collections import deque
from copy import deepcopy
from aoc2019.intcode import VM
from lattice import Point


COMMANDS = dict(zip((3, 1, 2, 4), Point(0, 0).adjacent()))
START = Point(0, 0)


def solve(data: str):
    ship_map = make_map(data)
    oxygen = next(pt for pt, val in ship_map.items() if val == 2)

    dist = flood(ship_map, START, oxygen)
    print(dist[oxygen])

    dist = flood(ship_map, oxygen)
    print(max(dist.values()))


def make_map(data: str) -> dict[Point, int]:
    grid = {}
    todo = [(START, VM(data))]
    while todo:
        pos, droid = todo.pop()
        for n, offset in COMMANDS.items():
            pos_ = pos + offset
            if pos_ in grid:
                continue
            droid_ = deepcopy(droid)
            droid_.send(n)
            if (status := next(droid_)) is None:
                raise RuntimeError
            grid[pos_] = status
            if status:
                todo.append((pos_, droid_))
    return grid


def flood(
    ship_map: dict[Point, int], start: Point, end: Point | None = None
) -> dict[Point, int]:
    dist = {start: 0}
    todo = deque([start])
    while todo:
        pos = todo.popleft()
        if pos == end:
            break
        for a in pos.adjacent():
            if ship_map.get(a) and a not in dist:
                dist[a] = dist[pos] + 1
                todo.append(a)
    return dist


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
