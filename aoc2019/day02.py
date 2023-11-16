from itertools import product
from aoc2019.intcode import VM


def solve(data: str) -> None:
    def alarm(noun: int, verb: int):
        vm = VM(data)
        vm[1] = noun
        vm[2] = verb
        next(vm, None)
        return vm[0]
    
    print(alarm(12, 2))

    target = 19690720
    n, v = next(p for p in product(range(100), repeat=2) if alarm(*p) == target)
    print(100*n + v)
    


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
