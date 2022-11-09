from heapq import heappop, heappush
from itertools import product
from utils import *


def solve(data: str) -> None:
    best_risk(data, 1)
    best_risk(data, 5)


def best_risk(data, n):
    grid = to_grid(data, int)
    rows, cols = (x+1 for x in max(grid))
    for pt, val in grid.copy().items():
        for r, c in product(range(n), repeat=2):
            if r == c == 0:
                continue
            pt_ = Point(pt.x + c * cols, pt.y + r * rows)
            val_ = val + r + c
            while val_ > 9:
                val_ -= 9
            grid[pt_] = val_
    visited = set()
    m = max(grid)
    pq = [(0, Point(0, 0))]
    while pq:
        risk, pt = heappop(pq)
        if pt in visited:
            continue
        visited.add(pt)
        if pt == m:
            print(risk)
            break
        for a in adjacent(pt):
            if a in grid and a not in visited:
                heappush(pq, (risk + grid[a], a))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
