from collections import defaultdict, deque
from typing import Iterator, Literal, TextIO, overload


class VM:
    def __init__(self, data: str, *vals: int) -> None:
        self.memory = defaultdict(int, enumerate(map(int, data.split(","))))
        self._pc = 0
        self._input = deque(vals)
        self._relative_base = 0

    @overload
    def _scan(self) -> int:
        ...

    @overload
    def _scan(self, n: Literal[1], mode: int) -> int:
        ...

    @overload
    def _scan(self, n: Literal[2], mode: int) -> tuple[int, int]:
        ...

    @overload
    def _scan(self, n: Literal[3], mode: int) -> tuple[int, int, int]:
        ...

    def _scan(self, n=1, mode=0):
        vals = []
        for _ in range(n):
            val = self._pc
            self._pc += 1
            mode, m = divmod(mode, 10)
            if m != 1:
                val = self.memory[val]
            if m == 2:
                val += self._relative_base
            vals.append(val)
        return vals[0] if n == 1 else tuple(vals)

    def __iter__(self) -> Iterator[int | None]:
        return self

    def __next__(self) -> int | None:
        while True:
            mode, op = divmod(self._scan(), 100)
            if op == 99:
                self._pc -= 1
                raise StopIteration
            elif op == 1:
                a, b, c = self._scan(3, mode)
                self.memory[c] = self.memory[a] + self.memory[b]
            elif op == 2:
                a, b, c = self._scan(3, mode)
                self.memory[c] = self.memory[a] * self.memory[b]
            elif op == 3:
                if not self._input:
                    self._pc -= 1
                    return
                a = self._scan(1, mode)
                self.memory[a] = self._input.popleft()
            elif op == 4:
                a = self._scan(1, mode)
                return self.memory[a]
            elif op == 5:
                a, b = self._scan(2, mode)
                if self.memory[a]:
                    self._pc = self.memory[b]
            elif op == 6:
                a, b = self._scan(2, mode)
                if not self.memory[a]:
                    self._pc = self.memory[b]
            elif op == 7:
                a, b, c = self._scan(3, mode)
                self.memory[c] = int(self.memory[a] < self.memory[b])
            elif op == 8:
                a, b, c = self._scan(3, mode)
                self.memory[c] = int(self.memory[a] == self.memory[b])
            elif op == 9:
                a = self._scan(1, mode)
                self._relative_base += self.memory[a]
            else:
                raise ValueError(f"unknown op: {op}")

    def send(self, *vals: int) -> None:
        self._input.extend(vals)
    
    def ascii(self, inp: TextIO, out: TextIO) -> Iterator[int]:
        for val in self:
            if val is None:
                line = inp.readline()
                if not line.endswith('\n'):
                    line += '\n'
                self.send(*map(ord, line))
            elif val in range(128):
                out.write(chr(val))
            else:
                yield val