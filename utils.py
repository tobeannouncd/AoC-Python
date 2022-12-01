from math import gcd
from numbers import Real
import re
from typing import Callable, Iterator, Mapping, NamedTuple, TypeVar


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return type(self)(*(s + o for s, o in zip(self, other)))

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return type(self)(*(s - o for s, o in zip(self, other)))

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return type(self)(self.x * other, self.y * other)

    def __floordiv__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return type(self)(self.x // other, self.y // other)

    def __pos__(self):
        return self

    def __neg__(self):
        return type(self)(-self.x, -self.y)

    def cw(self):
        return type(self)(-self.y, self.x)

    def ccw(self):
        return type(self)(self.y, -self.x)

    def unit(self):
        g = gcd(self.x, self.y)
        return type(self)(self.x // g, self.y // g)

    def adjacent(self, eight=False):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == dy == 0:
                    continue
                if eight or 0 in (dx, dy):
                    yield type(self)(self.x + dx, self.y + dy)


GridVal = TypeVar('GridVal')


def to_grid(data: str,
            f: Callable[[str], GridVal] = str) -> dict[Point, GridVal]:
    grid = {}
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            grid[Point(x, y)] = f(val)
    return grid


def grid_string(grid: Mapping[tuple[int, int], GridVal],
                f: Callable[[GridVal], str] = str,
                default=' ') -> str:
    xs, ys = map(sorted, zip(*grid))
    rows = []
    for y in range(ys[0], ys[-1] + 1):
        row = ''
        for x in range(xs[0], xs[-1] + 1):
            if (x, y) in grid:
                row += f(grid[x, y])
            else:
                row += default
        rows.append(row)
    return '\n'.join(rows)

def to_ints(data: str):
    return list(map(int, re.findall(r'-?\d+', data)))

def split_paragraphs(data: str):
    return data.split('\n\n')
