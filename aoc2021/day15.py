from heapq import heapify, heappop, heappush
from itertools import product

from lattice import from_str, Point


def solve(data) -> None:
    best_risk(data, 1)
    best_risk(data, 5)


def best_risk(data, n):
    # grid = to_grid(data, int)
    grid = {pt:int(val) for pt,val in from_str(data)}
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
    pq = []
    heappush(pq, (0, Point(0, 0)))
    while pq:
        risk, pt = heappop(pq)
        if pt in visited:
            continue
        visited.add(pt)
        if pt == m:
            print(risk)
            break
        # for a in adjacent(pt):
        for a in pt.adjacent():
            if a in grid and a not in visited:
                heappush(pq, (risk + grid[a], a))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
