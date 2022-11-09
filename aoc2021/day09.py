from math import prod
from utils import *


def solve(data: str) -> None:
    grid = {k: int(v) for k, v in to_grid(data).items()}
    low_points = {
        k
        for k, v in grid.items()
        if all(v < grid.get(a, 9) for a in adjacent(k))
    }
    print(sum(grid[p] + 1 for p in low_points))

    basins = []
    for p in low_points:
        visited = set()
        stack = [p]
        while stack:
            p = stack.pop()
            visited.add(p)
            stack.extend(
                a for a in adjacent(p)
                if a not in visited.union(stack) and grid.get(a, 9) < 9)
        basins.append(len(visited))
    basins.sort()
    print(prod(basins[-3:]))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
