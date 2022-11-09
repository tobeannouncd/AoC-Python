from utils import *
import re

def nice(s: str) -> bool:
    try:
        assert sum(1 for c in s if c in 'aeiou') >= 3
        assert re.search(r'(.)\1', s)
        assert all(x not in s for x in ['ab', 'cd', 'pq', 'xy'])
        return True
    except AssertionError:
        return False

def nice2(s: str) -> bool:
    try:
        assert re.search(r'(..).*\1', s)
        assert re.search(r'(.).\1', s)
        return True
    except AssertionError:
        return False

def solve(data: str) -> None:
    strings = data.splitlines()
    print(sum(1 for s in strings if nice(s)))
    print(sum(1 for s in strings if nice2(s)))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
