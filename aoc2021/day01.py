import aocd

nums = aocd.numbers


def solve(nums, size):
    return sum(1 for a, b in zip(nums, nums[size:]) if a < b)


print(solve(nums, 1))
print(solve(nums, 3))
