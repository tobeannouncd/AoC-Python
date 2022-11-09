from functools import reduce
from itertools import permutations
import json
import math
from utils import *


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, a, right = explode(a, n - 1)
    if exp:
        return True, left, [a, add_left(b, right)], None
    exp, left, b, right = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, left), b], right
    return False, None, x, None


def add_left(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x + n
    return [add_left(x[0], n), x[1]]

def add_right(x, n):
    if n is None:
        return x
    if isinstance(x, int):
        return x+n
    return [x[0], add_right(x[1], n)]

def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x//2, math.ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x

def magnitude(x):
    if isinstance(x, int):
        return x
    return 3*magnitude(x[0]) + 2*magnitude(x[1])

def solve(data: str) -> None:
    nums = [json.loads(line) for line in data.splitlines()]
    print(magnitude(reduce(add, nums)))
    print(max(magnitude(add(a,b)) for a,b in permutations(nums,2)))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
