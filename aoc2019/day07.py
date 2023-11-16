from itertools import cycle, permutations
from typing import Iterable

from aoc2019.intcode import VM


def solve(data: str) -> None:
    def amplify(phases: Iterable[int]) -> int:
        amps = (VM(data, phase) for phase in phases)

        signal = 0
        for amp in cycle(amps):
            if (x := next(amp.send(signal), None)) is None:
                break
            signal = x
        return signal
    
    for r in range(5), range(5, 10):
        print(max(amplify(p) for p in permutations(r)))


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
