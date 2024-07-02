def solve(data: str) -> None:
    strings = data.splitlines()

    print(sum(
        len(s) - len(eval(s))
        for s in strings
    ))

    print(sum(
        s.count('"') + s.count('\\') + 2
        for s in strings
    ))


if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
