from collections import defaultdict
from itertools import product

from parsing import integers


def solve(data) -> None:
    steps = {}
    for line in data.splitlines()[:-2]:
        xa, xb, ya, yb, za, zb = integers(line)
        if xa not in range(-50, 51):
            break
        for x, y, z, in product(range(xa, xb+1),
                                range(ya, yb+1),
                                range(za, zb+1)):
            steps[x,y,z] = line.split()[0]
    print(sum(1 for v in steps.values() if v=='on'))



def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
