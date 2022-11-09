from collections import Counter
from utils import *


def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0


def solve(data: str) -> None:
    lines = []
    for line in data.splitlines():
        x, y, X, Y = to_ints(line)
        a = Point(x, y)
        b = Point(X, Y)
        lines.append((a, b))
    ortho = [(a, b) for a, b in lines if 0 in a - b]
    grid = Counter()
    draw_lines(ortho, grid)
    print(sum(1 for v in grid.values() if v > 1))
    diag = [l for l in lines if l not in ortho]
    draw_lines(diag, grid)
    print(sum(1 for v in grid.values() if v > 1))


def draw_lines(lines, grid):
    for a, b in lines:
        d = Point(*map(sign, b - a))
        grid[a] += 1
        while a != b:
            a += d
            grid[a] += 1


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
