from utils import *


def fuel(start, end):
    d = abs(start - end)
    return d * (d + 1) // 2


def solve(data: str) -> None:
    crabs = sorted(to_ints(data))
    N = len(crabs)
    tgt = crabs[N // 2]
    print(sum(abs(crab - tgt) for crab in crabs))

    tgt = sum(crabs) // N
    print(sum(fuel(crab, tgt) for crab in crabs))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
