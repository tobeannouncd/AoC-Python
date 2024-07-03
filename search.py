from collections import deque
from typing import Callable, Hashable, Iterable, Iterator, Optional, TypeVar, cast
from priority_queue import PQueue

_T = TypeVar('_T')
_Cost = TypeVar('_Cost', float, int)

def bfs(start: _T | Iterable[_T],
        neighbors: Callable[[_T], Iterable[_T]],
        multiple: bool=False,
        key: Optional[Callable[[_T], Hashable]]=None
        ) -> Iterator[_T]:
    """Yields nodes in order of traversal via breadth-first search"""
    if key is None:
        key = lambda x: x
    queue = deque(cast(Iterable[_T], start) if multiple else [cast(_T, start)])
    visited = set()
    while queue:
        current = queue.popleft()
        r = key(current)
        if r in visited: continue
        yield current
        visited.add(r)
        queue.extend(neighbors(current))

def dijkstra(start: _T | Iterable[_T],
             neighbors: Callable[[_T], Iterable[_T]],
             cost: Callable[[_T, _T], _Cost],
             multiple: bool=False,
             key: Optional[Callable[[_T], Hashable]]=None
             ) -> Iterator[tuple[_Cost, _T]]:
    h = lambda _: cast(_Cost, 0)
    return a_star(start, neighbors, cost, h, multiple, key)


def a_star(start: _T | Iterable[_T],
           neighbors: Callable[[_T], Iterable[_T]],
           cost: Callable[[_T, _T], _Cost],
           heuristic: Callable[[_T], _Cost],
           multiple: bool=False,
           key: Optional[Callable[[_T], Hashable]]=None
           ) -> Iterator[tuple[_Cost, _T]]:
    """Yields `(cost, node)` pairs in order of traversal via A*"""
    if key is None:
        key = lambda x: x
    queue = PQueue(
        (heuristic(x), (cast(_Cost, 0), x))
        for x in (cast(Iterable[_T], start) if multiple else
                  [cast(_T, start)]
                  )
        )
    visited = set()
    while queue:
        _, (c, here) = queue.pop()
        r = key(here)
        if r in visited: continue
        yield c, here
        for there in neighbors(here):
            c_there = c + cost(here, there)
            p = heuristic(there) + c_there
            queue.push(p, (c_there, there))