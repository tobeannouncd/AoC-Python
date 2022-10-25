from collections import defaultdict, deque
from sys import stdin, stdout
from typing import TextIO

__all__ = ['Intcode', 'HaltProgram', 'NoInput']


def parse(data: str):
    return list(map(int, data.split(',')))


class HaltProgram(Exception):
    pass


class NoInput(Exception):
    pass


class Intcode:

    def __init__(self, data: str) -> None:
        self._memory = defaultdict(int, enumerate(parse(data)))
        self._pointer = 0
        self._relative_base = 0
        self._input = deque()

    def __getitem__(self, i: int) -> int:
        return self._memory[i]

    def __setitem__(self, i: int, val: int):
        self._memory[i] = val

    def _scan(self, n: int = 1, mode: int = 0):
        for _ in range(n):
            mode, m = divmod(mode, 10)
            val = self._pointer
            self._pointer += 1
            if m != 1:
                val = self[val]
            if m == 2:
                val += self._relative_base
            yield val

    def _step(self):
        x, = self._scan()
        mode, opcode = divmod(x, 100)
        if opcode == 99:
            self._pointer -= 1
            raise HaltProgram
        elif opcode == 1:
            a, b, c = self._scan(3, mode)
            self[c] = self[a] + self[b]
        elif opcode == 2:
            a, b, c = self._scan(3, mode)
            self[c] = self[a] * self[b]
        elif opcode == 3:
            if not self._input:
                self._pointer -= 1
                raise NoInput
            a, = self._scan(1, mode)
            self[a] = self._input.popleft()
        elif opcode == 4:
            a, = self._scan(1, mode)
            return self[a]
        elif opcode == 5:
            a, b = self._scan(2, mode)
            if self[a]:
                self._pointer = self[b]
        elif opcode == 6:
            a, b = self._scan(2, mode)
            if not self[a]:
                self._pointer = self[b]
        elif opcode == 7:
            a, b, c = self._scan(3, mode)
            self[c] = int(self[a] < self[b])
        elif opcode == 8:
            a, b, c = self._scan(3, mode)
            self[c] = int(self[a] == self[b])
        elif opcode == 9:
            a, = self._scan(1, mode)
            self._relative_base += self[a]
        else:
            raise ValueError(f'invalid opcode: {opcode}')

    def run(self):
        while True:
            try:
                self._step()
            except HaltProgram:
                break

    def write(self, val: int):
        self._input.append(val)

    def read(self, n: int = -1) -> list[int]:
        out = []
        while n:
            try:
                x = self._step()
                if x is not None:
                    out.append(x)
                    n -= 1
            except HaltProgram:
                break
        return out
    
    def ascii(self, inp: TextIO = stdin, out: TextIO = stdout):
        while True:
            try:
                x = self.read(1)
                if not x:
                    break
                val, = x
                if val in range(128):
                    out.write(chr(val))
                else:
                    return val
            except NoInput:
                s = inp.readline().strip() + '\n'
                for o in map(ord, s):
                    self.write(o)