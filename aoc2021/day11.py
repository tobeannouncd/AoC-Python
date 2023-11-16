from itertools import count

import numpy as np


@np.vectorize
def reset(x):
    return x if x < 10 else 0


def simulate(octopi: np.ndarray):
    R, C = octopi.shape
    octopi += 1
    flashed = set()
    while True:
        changed = False
        for i, j in np.argwhere(octopi >= 10):
            if (i, j) in flashed:
                continue
            changed = True
            flashed.add((i, j))
            s = slice(max(0, i - 1), min(R, i + 2)), slice(max(0, j - 1), min(C, j + 2))
            octopi[s] += 1
        if not changed:
            break
    octopi[:] = reset(octopi)


def solve(data: str) -> None:
    octopi = np.array([[int(x) for x in line] for line in data.splitlines()])

    flashes = 0
    for _ in range(100):
        simulate(octopi)
        flashes += np.count_nonzero(octopi == 0)
    print(flashes)

    for t in count(101):
        simulate(octopi)
        if not np.count_nonzero(octopi):
            print(t)
            break


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
