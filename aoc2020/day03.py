from math import prod
from lattice import Point, from_str


def count_trees(hill: dict[Point,str], slope: Point) -> int:
    x_max = max(p.x for p in hill)
    dx = Point(-1 - x_max, 0)
    pos = Point(0, 0)
    ans = 0
    while pos in hill:
        ans += hill[pos] == '#'
        pos += slope
        while pos.x > x_max:
            pos += dx
    return ans


def solve(data) -> None:
    hill = dict(from_str(data.rstrip()))
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
