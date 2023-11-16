from aoc2019.intcode import VM


def solve(data: str) -> None:
    vm = VM(data)
    for x in 1, 5:
        *vals, ans = vm.reset().send(x).get()
        assert not any(v for v in vals)
        print(ans)


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
