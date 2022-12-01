from functools import partial


def is_valid(part, policy: str):
    rng, ch, pwd = policy.strip().split()
    a, b = map(int, rng.split('-'))
    ch = ch.strip(':')
    if part == 1:
        return pwd.count(ch) in range(a, b + 1)
    return (pwd[a - 1] == ch) ^ (pwd[b - 1] == ch)


def solve(data: str) -> None:
    print(sum(1 for _ in filter(partial(is_valid, 1), data.splitlines())))
    print(sum(1 for _ in filter(partial(is_valid, 2), data.splitlines())))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
