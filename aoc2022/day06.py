from itertools import count


def solve(data: str) -> None:
    for n in 4, 14:
        print(next(i+n for i in count() if len(set(data[i:i+n])) == n))


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
