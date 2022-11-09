from typing import MutableMapping

from utils import *


def simulate(grid: MutableMapping[Point, int]) -> int:
    flashed = set()
    for k in grid:
        grid[k] += 1
    while True:
        flashes = 0
        for k, v in grid.items():
            if v > 9 and k not in flashed:
                flashed.add(k)
                flashes += 1
                for a in adjacent(k, 8):
                    if a in grid:
                        grid[a] += 1
        if not flashes:
            break
    for k in flashed:
        grid[k] = 0
    return len(flashed)


def solve(data: str) -> None:
    grid = to_grid(data, int)
    steps = 100
    flashes = 0
    for _ in range(steps):
        flashes += simulate(grid)
    print(flashes)

    while True:
        steps += 1
        s = simulate(grid)
        if s == len(grid):
            print(steps)
            break


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
