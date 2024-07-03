

from dataclasses import dataclass, field, astuple
from heapq import heappop, heappush
from typing import Generic, Iterable, Optional, Self, TypeVar, overload
from collections.abc import Sequence

_T = TypeVar('_T')

@dataclass(order=True)
class _Item(Generic[_T]):
    priority: float
    item: _T = field(compare=False)

class PQueue(Sequence[_T]):
    def __init__(self, iterable: Optional[Iterable[tuple[float, _T]]]=None) -> None:
        self._heap: list[_Item[_T]] = []
        for p, item in (iterable or []):
            heappush(self._heap, _Item(p, item))

    def pop(self) -> tuple[float, _T]:
        return astuple(heappop(self._heap))

    def push(self, priority: float, item: _T) -> None:
        heappush(self._heap, _Item(priority, item))

    def __repr__(self):
        return "PQueue({})".format(list(map(astuple, self._heap)))

    @overload
    def __getitem__(self, index: int) -> _T: ...
    @overload
    def __getitem__(self, index: slice) -> Self: ...
    def __getitem__(self, index):
        if isinstance(index, int):
            return self._heap[index].item
        return PQueue(map(astuple, self._heap[index]))

    def __len__(self):
        return len(self._heap)


