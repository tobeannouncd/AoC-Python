from aoc2019.intcode import VM


def solve(data: str) -> None:
    for inp in 1, 2:
        *errors, code = VM(data, inp)
        if errors or code is None:
            raise RuntimeError(f"{(*errors, code)=}")
        print(code)


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
