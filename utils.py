from collections import deque, namedtuple
from heapq import heappop, heappush
from numbers import Real
from typing import Callable, Hashable, Iterable, Literal, Mapping, Optional, Protocol, TypeVar

__all__ = ['Point', 'grid_string', 'bfs']


class Point(namedtuple('Point', 'x,y')):

    def __add__(self, __o: 'Point') -> 'Point':
        return Point(self.x + __o.x, self.y + __o.y)

    def __sub__(self, __o: 'Point') -> 'Point':
        return Point(self.x - __o.x, self.y - __o.y)

    def __abs__(self):
        return sum(map(abs, self))

    def cw(self) -> 'Point':
        return Point(-self.y, self.x)

    def ccw(self) -> 'Point':
        return Point(self.y, -self.x)


def grid_string(grid: Mapping[tuple[int, int], str],
                default: str = ' ') -> str:
    xs, ys = map(sorted, zip(*grid))
    rows = []
    for y in range(ys[0], ys[-1] + 1):
        row = ''
        for x in range(xs[0], xs[-1] + 1):
            row += grid.get((x, y), default)
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