from collections import Counter
from utils import *


def solve(data: str) -> None:
    lanternfish = Counter(to_ints(data))
    simulate(lanternfish, 80)
    print(sum(lanternfish.values()))
    simulate(lanternfish, 256 - 80)
    print(sum(lanternfish.values()))


def simulate(state, days):
    for _ in range(days):
        for k, v in state.copy().items():
            state[k] -= v
            if k == 0:
                state[6] += v
                state[8] += v
            else:
                state[k - 1] += v


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
