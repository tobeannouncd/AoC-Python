from typing import Callable, Iterable, TextIO
from point import dict_to_string


Pt = tuple[int, int]
Instruction = tuple[Callable[...,None], list[int]]


class CRT:
    def __init__(self, width=40) -> None:
        self.x = 1
        self.cycle = 0
        self.width = width
        self.pixels: set[Pt] = set()
    
    @property
    def screen(self):
        return dict_to_string(dict.fromkeys(self.pixels, '#'))


    def run(self, signal: TextIO) -> None:
        queue = []
        while True:
            self.cycle += 1
            if not queue:
                command = signal.readline()
                if not command:
                    break
                queue.extend(self._parse(command))
            self._cycle(queue.pop())

    def _parse(self, s: str) -> Iterable[Instruction]:
        match s.split():
            case ["noop"]:
                yield self._noop, []
            case ["addx", n]:
                yield self._addx, [int(n)]
                yield self._noop, []

    def _noop(self) -> None:
        pass

    def _addx(self, n: int) -> None:
        self.x += n

    def _cycle(self, i: Instruction) -> None:
        self._scan()
        f, args = i
        f(*args)

    def _scan(self):
        y, x = divmod(self.cycle-1, self.width)
        if x in range(self.x-1, self.x + 2):
            self.pixels.add((x,y))
