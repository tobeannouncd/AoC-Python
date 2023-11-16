from array import array
from collections import deque
from collections.abc import Iterator
from io import StringIO
from operator import add, eq, lt, mul
from typing import Generator, Literal, Optional, Self, TextIO, overload


class VM(Iterator[int | None]):
    def __init__(self, s: str, *values: int):
        self._prog: array[int] = array("q", (int(x) for x in s.split(",")))
        self._mem: dict[int, int] = {}
        self._pc: int = 0
        self._rb: int = 0
        self._inp: deque[int] = deque(values)

    def reset(self) -> Self:
        self._mem.clear()
        self._pc = 0
        self._rb = 0
        self._inp.clear()
        return self

    def __getitem__(self, index: int) -> int:
        if index < 0:
            raise IndexError("negative index")
        if (val := self._mem.get(index)) is None:
            try:
                val = self._prog[index]
            except IndexError:
                val = 0
        return val

    def __setitem__(self, index: int, value: int):
        self._mem[index] = value

    @overload
    def _scan(self) -> int:
        ...

    @overload
    def _scan(self, mode: int) -> int:
        ...

    @overload
    def _scan(self, mode: int, n: int) -> list[int]:
        ...

    def _scan(self, mode=0, n=None):
        vals = []
        for _ in range(1 if n is None else n):
            x = self._pc
            self._pc += 1
            mode, m = divmod(mode, 10)
            if m != 1:
                x = self[x]
            if m == 2:
                x += self._rb
            vals.append(x)
        return vals[0] if n is None else vals

    def __next__(self) -> int | None:
        while True:
            mode, op = divmod(self._scan(), 100)
            if op == 99:
                self._pc -= 1
                break
            elif op in (1, 2):
                a, b, c = self._scan(mode, 3)
                self[c] = [add, mul][op - 1](self[a], self[b])
            elif op == 3:
                if not self._inp:
                    self._pc -= 1
                    return
                a = self._scan(mode)
                self[a] = self._inp.popleft()
            elif op == 4:
                a = self._scan(mode)
                return self[a]
            elif op in (5, 6):
                a, b = self._scan(mode, 2)
                if bool(self[a]) ^ (op == 6):
                    self._pc = self[b]
            elif op in (7, 8):
                a, b, c = self._scan(mode, 3)
                self[c] = int([lt, eq][op - 7](self[a], self[b]))
            elif op == 9:
                a = self._scan(mode)
                self._rb += self[a]
            else:
                raise NotImplementedError(f"{op=}")
        raise StopIteration

    def send(self, *values: int) -> Self:
        self._inp.extend(values)
        return self
    
    @overload
    def get(self) -> list[int]:
        ...

    @overload
    def get(self, n: Literal[1]) -> int:
        ...

    @overload
    def get(self, n: int) -> list[int]:
        ...
    
    def get(self, n=-1):
        vals = []
        rem = n
        while rem:
            rem -= 1
            if (x := next(self, None)) is None:
                break
            vals.append(x)
        return vals[0] if n == 1 else vals
        

    
    def ascii(self, inp: Optional[TextIO] = None, out: Optional[TextIO] = None) -> Iterator[int]:
        inp = inp or StringIO()
        out = out or StringIO()
        for x in self:
            if x is None:
                line = inp.readline().strip()
                self._inp.extend(map(ord, line+'\n'))
            elif x in range(128):
                out.write(chr(x))
            else:
                yield x