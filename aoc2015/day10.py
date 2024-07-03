from itertools import groupby
from typing import Iterable, Iterator


def solve(data: str) -> None:
    seq = list(map(int, data.strip()))
    for n in 40, 10:
        for _ in range(n):
            seq = list(look_and_say(seq))
        print(len(seq))

def look_and_say(seq: Iterable[int]) -> Iterator[int]:
    for k, g in groupby(seq):
        n = len(list(g))
        yield n
        yield k


if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
