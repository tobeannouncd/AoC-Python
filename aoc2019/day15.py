from collections import deque
from copy import deepcopy

from aoc2019.intcode import VM
from lattice import Point

MOVES = {
    1: Point(0, -1),
    2: Point(0, 1),
    3: Point(-1, 0),
    4: Point(1, 0),
}


def solve(data: str) -> None:
    scan = make_map(data)
    goal = next(pt for pt, s in scan.items() if s == 2)

    print(flood(scan, Point(0, 0))[goal])
    print(max(flood(scan, goal).values()))


def make_map(data):
    scan = {}
    todo = [(VM(data), Point(0, 0))]
    while todo:
        bot, pos = todo.pop()
        for cmd, x in MOVES.items():
            if (nxt := pos + x) in scan:
                continue
            scan[nxt] = status = (b := deepcopy(bot).send(cmd)).get(1)
            if status:
                todo.append((b, nxt))
    return scan


def flood(scan, start):
    dist = {start: 0}
    todo = deque([start])
    while todo:
        pos = todo.popleft()
        for nxt in pos.adjacent():
            if nxt not in dist and scan.get(nxt):
                dist[nxt] = dist[pos] + 1
                todo.append(nxt)
    return dist


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
