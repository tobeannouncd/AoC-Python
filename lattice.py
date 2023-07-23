from dataclasses import dataclass
from itertools import product
from typing import Iterable, Iterator, Literal, Self


@dataclass(frozen=True, order=True, slots=True)
class Point:
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Point):
            return self.__class__(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, Point):
            return self.__class__(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int) -> Self:
        if isinstance(other, int):
            return self.__class__(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other: int) -> Self:
        return self * other

    def __floordiv__(self, other: int) -> Self:
        if isinstance(other, int):
            return self.__class__(self.x // other, self.y // other)
        return NotImplemented

    def __abs__(self) -> int:
        return abs(self.x) + abs(self.y)

    def rot_cw(self) -> Self:
        return self.__class__(-self.y, self.x)

    def rot_ccw(self) -> Self:
        return self.__class__(self.y, -self.x)

    def __iter__(self) -> Iterator[int]:
        yield self.x
        yield self.y

    def sign(self) -> Self:
        return self.__class__(_sign(self.x), _sign(self.y))

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
    
    def adjacent(self, n: Literal[4,5,8,9] = 4) -> Iterator[Self]:
        for dx, dy in product(range(-1, 2), repeat=2):
            if (dx or dy or n & 1) and (not dx*dy or n & 8):
                yield self.__class__(self.x + dx, self.y + dy)


def _sign(n: int) -> int:
    return n // abs(n) if n else n


def from_str(string: str) -> Iterator[tuple[Point, str]]:
    for y, line in enumerate(string.splitlines()):
        for x, val in enumerate(line):
            yield Point(x, y), val


def to_str(points: Iterable[Point], val: str = '#', empty: str = ' ') -> str:
    if len(val) != 1 or len(empty) != 1:
        raise ValueError("`val` and `empty` must be single character strings")
    xs, ys = zip(*points)
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    rows = ymax - ymin + 1
    cols = xmax - xmin + 1
    out = [[empty]*cols for _ in range(rows)]
    for x, y in zip(xs, ys):
        out[y-ymin][x-xmin] = val
    return '\n'.join(''.join(row) for row in out)


def main():
    ...


if __name__ == "__main__":
    main()
