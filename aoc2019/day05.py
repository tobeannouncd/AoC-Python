from aoc2019.intcode import VM



def solve(data):
    for inp in 1, 5:
        *errors, code = VM(data, inp)
        assert all(not x for x in errors)
        print(code)


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
