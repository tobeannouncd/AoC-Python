from itertools import product
from aoc2019.intcode import VM


def solve(data: str):
    print(alarm(data, 12, 2))
    
    n, v = next((n,v) for n,v in product(range(100), repeat=2) if alarm(data, n, v) == 19690720)
    print(100*n + v)
    

def alarm(data: str, noun: int, verb: int) -> int:
    pc = VM(data)
    pc.memory[1] = noun
    pc.memory[2] = verb
    next(pc, None)
    return pc.memory[0]



if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
