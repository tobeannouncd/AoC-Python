from itertools import product

from aoc2019.intcode import VM


def solve(data: str) -> None:
    drone_system = VM(data)

    def is_pulled(x, y):
        return bool(drone_system.reset().send(x, y).get(1))

    print(sum(1 for x, y in product(range(50), repeat=2) if is_pulled(x, y)))

    x, y = 0, 0
    while not is_pulled(x, y+99):
        x += 1
        while not is_pulled(x+99, y):
            y += 1
    print(10000*x + y)


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
