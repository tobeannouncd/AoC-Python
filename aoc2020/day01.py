from math import prod
from typing import Iterable
from utils import ints

def two_sum(target: int, nums: Iterable[int]):
    seen = set()
    for n in nums:
        if target - n in seen:
            return n, target-n
        seen.add(n)

def three_sum(target: int, nums: Iterable[int]):
    seen = set()
    for n in nums:
        x = two_sum(target-n, seen)
        if x:
            return (n, *x)
        seen.add(n)

def solve(data: str) -> None:
    nums = ints(data)
    print(prod(two_sum(2020, nums) or (-1,)))
    print(prod(three_sum(2020, nums) or (-1,)))



def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
