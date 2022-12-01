from math import prod
from utils import Point, to_grid


def count_trees(hill, slope: Point) -> int:
    x_max = max(p.x for p in hill)
    dx = Point(-x_max - 1, 0)
    pos = Point(0, 0)
    ans = 0
    while pos in hill:
        ans += hill[pos] == '#'
        pos += slope
        while pos.x > x_max:
            pos += dx
    return ans


def solve(data: str) -> None:
    hill = to_grid(data)
    print(count_trees(hill, Point(3, 1)))
    print(
        prod(
            count_trees(hill, Point(dx, dy))
            for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
