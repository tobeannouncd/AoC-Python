from itertools import product
from operator import itemgetter
from typing import Callable, Iterable, Iterator, Mapping, Optional, TypeVar

_Pt = tuple[int, int]


def adjacent(p: _Pt, diagonal=False) -> Iterator[_Pt]:
    x, y = p
    for dy, dx in product(range(-1, 2), repeat=2):
        if (dx, dy) != (0, 0) and (diagonal or not dx * dy):
            yield (x + dx, y + dy)


def rotate_cw(p: _Pt) -> _Pt:
    x, y = p
    return -y, x


def rotate_ccw(p: _Pt) -> _Pt:
    x, y = p
    return y, -x


def add(a: _Pt, b: _Pt) -> _Pt:
    return tuple(aa + bb for aa, bb in zip(a, b))


def sub(a: _Pt, b: _Pt) -> _Pt:
    return tuple(aa - bb for aa, bb in zip(a, b))


def scale(m: int, p: _Pt) -> _Pt:
    return tuple(m * a for a in p)


def manhattan(a: _Pt, b: _Pt) -> int:
    dx, dy = sub(a, b)
    return abs(dx) + abs(dy)


V = TypeVar("V")


def to_grid(s: str, *, f: Callable[[str], V] = str) -> dict[_Pt, V]:
    grid: dict[_Pt, V] = {}
    for y, line in enumerate(s.splitlines()):
        for x, val in enumerate(line):
            grid[x, y] = f(val)
    return grid


def dict_to_string(grid: Mapping[_Pt, V], *, f: Callable[[V], str] = str, default=" ") -> str:
    xs, ys = map(sorted, zip(*grid))
    rows: list[str] = []
    for y in range(ys[0], ys[-1] + 1):
        row = ""
        for x in range(xs[0], xs[-1] + 1):
            if (x, y) in grid:
                row += f(grid[x, y])
            else:
                row += default
        rows.append(row + "\n")
    return "".join(rows)


    


