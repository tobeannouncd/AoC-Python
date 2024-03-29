from parsing import integers

def solve(data) -> None:
    nums = integers(data)
    print(sum(1 for a, b in zip(nums, nums[1:]) if a < b))
    print(sum(1 for a, b in zip(nums, nums[3:]) if a < b))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
