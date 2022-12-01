from typing import Callable, Iterable


def solve(data: str) -> None:
    print(go(data, any))
    print(go(data, all))


def go(data: str, f: Callable[[Iterable], bool]):
    tot = 0
    for group in data.split('\n\n'):
        tot += sum(1 for x in set(group)
                   if f(x in line for line in group.splitlines()))
    return tot


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
