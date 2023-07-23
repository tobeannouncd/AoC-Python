from itertools import cycle, permutations
from aoc2019.intcode import VM


def solve(data: str) -> None:
    def amplify(*phases: int) -> int:
        amps = (VM(data, phase) for phase in phases)
        signal = 0
        for amp in cycle(amps):
            amp.send(signal)
            x = next(amp, None)
            if x is None:
                return signal
            signal = x
        raise RuntimeError
            
    for rng in range(5), range(5, 10):
        print(max(amplify(*p) for p in permutations(rng)))
    


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
