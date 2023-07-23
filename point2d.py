from math import gcd
from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    Mapping,
    NamedTuple,
    Optional,
    Self,
    TypeVar,
)


class Pt(NamedTuple):
    """Class representing 2D lattice points.

    `Pt(x: int, y: int)` -> `Pt(x, y)`

    The following operations differ from standard tuple behavior:
        `self + other`: Returns the vector sum of self and other.
        `self * other`: Return self scaled by integer other.
        `other * self`: Return self scaled by integer other.
        `<,<=,>,>=,==,!=`: Compares two Pt instances based on reading order (left to right (+x) -> top to bottom (+y)).

    The additional special methods implement the following behavior:
        `complex(self)`: Returns complex(self.x, self.y).
        `self @ other`: Returns the dot product of self and other.
        `self // other`: Returns Pt(self.x // other, self.y // other).
        `abs(self)`: Returns the cartesian distance from Pt(0,0) to self as a float.
    """

    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        if isinstance(other, Pt):
            return Pt(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Self) -> Self:
        if isinstance(other, Pt):
            return Pt(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __lt__(self, other: Self) -> bool:
        if isinstance(other, Pt):
            return (self.y, self.x) < (other.y, other.x)
        return NotImplemented

    def __le__(self, other: Self) -> bool:
        if isinstance(other, Pt):
            return (self.y, self.x) <= (other.y, other.x)
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if isinstance(other, Pt):
            return (self.y, self.x) > (other.y, other.x)
        return NotImplemented

    def __ge__(self, other: Self) -> bool:
        if isinstance(other, Pt):
            return (self.y, self.x) >= (other.y, other.x)
        return NotImplemented

    def __eq__(self, other) -> bool:
        return isinstance(other, Pt) and (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __mul__(self, other: int) -> Self:
        if isinstance(other, int):
            return Pt(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other: int) -> Self:
        if isinstance(other, int):
            return Pt(other * self.x, other * self.y)
        return NotImplemented

    def __matmul__(self, other: Self) -> int:
        if isinstance(other, Pt):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __complex__(self):
        return complex(self.x, self.y)

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __floordiv__(self, other: int) -> Self:
        if isinstance(other, int):
            return Pt(self.x // other, self.y // other)
        return NotImplemented

    def cw(self, center: Optional[Self] = None) -> Self:
        p = self - (center or Pt(0, 0))
        return (center or Pt(0, 0)) + Pt(-p.y, p.x)

    def ccw(self, center: Optional[Self] = None) -> Self:
        p = self - (center or Pt(0, 0))
        return (center or Pt(0, 0)) + Pt(p.y, -p.x)

    def adjacent(self, diagonal=False) -> Iterator[Self]:
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if (dx, dy) != (0, 0) and (diagonal or not dx * dy):
                    yield Pt(self.x + dx, self.y + dy)


def str_to_points(s: str) -> Iterator[tuple[Pt, str]]:
    """Yields pairs of `(Pt, str)` corresponding to the coordinates of each character in s."""
    for y, line in enumerate(s.splitlines()):
        for x, char in enumerate(line):
            yield Pt(x, y), char


T = TypeVar("T")
Grid = Mapping[Pt, T] | Mapping[tuple[int, int], T]


def grid_to_string(
    grid: Grid[T], *, f: Optional[Callable[[T], str]] = None, fill=" "
) -> str:
    """Returns a string given a grid mapping points to values.

    Args:
        grid: An object mapping key => value. list(key) must return [x: int, y: int].
        f: A function that converts grid values to a single character string. If omitted or None, values are converted to the first character of the default string representation.
        fill: A single character string used to fill in gaps in the grid.
    """
    if f is None:
        f = lambda v: str(v)[0]
    if len(grid) == 0:
        return ""
    if len(grid) == 1:
        return f(next(v for v in grid.values()))
    (x_min, *_, x_max), (y_min, *_, y_max) = map(sorted, zip(*grid))
    rows, cols = y_max - y_min + 1, x_max - x_min + 1
    out = [[fill] * cols for _ in range(rows)]
    for (x, y), val in grid.items():
        row = y - y_min
        col = x - x_min
        out[row][col] = f(val)
    return "\n".join("".join(row) for row in out)


def points_between(point_a: Pt, point_b: Pt) -> Iterator[Pt]:
    """Yields the points with integer coordinates between point_a and point_b, inclusive."""
    if point_a == point_b:
        yield point_a
        return
    diff = point_b - point_a
    diff //= gcd(*diff)
    while True:
        yield point_a
        if point_a == point_b:
            break
        point_a += diff


def points_to_string(points: Iterable[tuple[int, int]], *, bg=" ", fg="\u2593") -> str:
    """Returns a string representation of the given points.

    If your points are representative of a single type of object, you can use this function instead of creating a mapping for `grid_to_string`.
    """
    return grid_to_string(dict.fromkeys(points, fg), fill=bg)
