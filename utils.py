from collections import deque
from heapq import heappop, heappush
from numbers import Real
import re
from typing import Callable, Hashable, Iterable, Iterator, Literal, Mapping, Optional, Protocol, TypeVar, NamedTuple, Self

__all__ = [
    'Point', 'grid_string', 'bfs', 'dijkstra', 'to_ints', 'to_grid', 'adjacent'
]


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, __o: Self) -> Self:
        return type(self)(self.x + __o.x, self.y + __o.y)

    def __sub__(self, __o: Self) -> Self:
        return type(self)(self.x - __o.x, self.y - __o.y)

    def __abs__(self) -> int:
        return abs(self.x) + abs(self.y)

    def cw(self) -> Self:
        return type(self)(-self.y, self.x)

    def ccw(self) -> Self:
        return type(self)(self.y, -self.x)


P = TypeVar('P', tuple[int, int], Point)


def grid_string(grid: Mapping[P, str], default: str = ' ') -> str:
    xs, ys = map(sorted, zip(*grid))
    rows = []
    grid_ = {(x, y): v for (x, y), v in grid.items()}
    for y in range(ys[0], ys[-1] + 1):
        row = ''
        for x in range(xs[0], xs[-1] + 1):
            row += grid_.get((x, y), default)
        rows.append(row)
    return '\n'.join(rows)


S = TypeVar('S', bound=Hashable)


def bfs(start: S, successors: Callable[[S], Iterable[S]],
        stop: Callable[[S], bool]):
    queue = deque([start])
    prev: dict[S, Optional[S]] = {start: None}
    dist = {start: 0}
    while queue:
        pos = queue.popleft()
        if stop(pos):
            break
        for p in successors(pos):
            if p not in prev:
                prev[p] = pos
                dist[p] = dist[pos] + 1
                queue.append(p)
    return prev, dist


H = TypeVar('H', bound='_Heapable')


class _Heapable(Protocol):

    def __hash__(self) -> int:
        ...

    def __eq__(self: H, __o: H) -> bool:
        ...

    def __lt__(self: H, __o: H) -> bool:
        ...


def dijkstra(start: H, successors: Callable[[H], Iterable[tuple[Real, H]]],
             stop: Callable[[H], bool]):
    pq = [(0, start)]
    prev: dict[H, Optional[H]] = {start: None}
    dist: dict[H, Real | Literal[0]] = {start: 0}
    visited = set()
    while pq:
        d, pos = heappop(pq)
        if pos in visited:
            continue
        visited.add(pos)
        if stop(pos):
            break
        for cost, p in successors(pos):
            d_ = d + cost
            if d_ < dist.get(p, float('inf')):
                prev[p] = pos
                dist[p] = d_
                heappush(pq, (d_, p))
    return prev, dist


def to_ints(s: str) -> list[int]:
    return list(map(int, re.findall(r'-?\d+', s)))


O = TypeVar('O')


def to_grid(data: str, f: Callable[[str], O] = str) -> dict[Point, O]:
    grid = {}
    for y, row in enumerate(data.splitlines()):
        for x, val in enumerate(row):
            grid[Point(x, y)] = f(val)
    return grid


def adjacent(p: Point, n: Literal[4, 8] = 4) -> Iterator[Point]:
    orth = Point(0, 1)
    diag = Point(1, 1)
    for _ in range(4):
        yield p + orth
        if n == 8:
            yield p + diag
        orth = orth.ccw()
        diag = diag.ccw()