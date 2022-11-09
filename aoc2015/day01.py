from utils import *


def solve(data: str) -> None:
    print(data.count('(') - data.count(')'))
    floor = 0
    for i, val in enumerate(data, start=1):
        if val == '(':
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            print(i)
            break


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
