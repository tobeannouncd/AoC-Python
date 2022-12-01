from collections import deque
from utils import to_ints


def twosum(nums, target):
    seen = set()
    for n in nums:
        if target - n in seen:
            return True
        seen.add(n)
    return False


def solve(data: str) -> None:
    nums = to_ints(data)
    window = deque(nums[:25], maxlen=25)
    target = -1
    for n in nums[25:]:
        if not twosum(window, n):
            target = n
            break
        window.append(n)
    print(target)
    i,j = 0, 1
    while sum(nums[i:j]) != target:
        j += 1
        while sum(nums[i:j]) > target:
            i += 1
    print(min(nums[i:j]) + max(nums[i:j]))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
