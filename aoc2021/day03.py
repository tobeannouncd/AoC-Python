from utils import *


def get_digit(nums, i, func):
    col = [n[i] for n in nums]
    return func(col, key=lambda x: (col.count(x), x))

def get_rating(nums, func):
    remaining = set(nums)
    i = 0
    while len(remaining) > 1:
        d = get_digit(remaining, i, func)
        remaining = {n for n in remaining if n[i]==d}
        i += 1
    return int(remaining.pop(), 2)



def solve(data: str) -> None:
    rows = data.splitlines()
    N = len(rows[0])
    gamma = ''.join(get_digit(rows,i, max) for i in range(N))
    epsilon = ''.join(get_digit(rows,i, min) for i in range(N))
    print(int(gamma,2)*int(epsilon,2))

    oxygen_rating = get_rating(rows,max)
    co2_rating = get_rating(rows,min)
    print(oxygen_rating*co2_rating)

def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
