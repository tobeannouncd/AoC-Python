from aoc2019.intcode import VM


def solve(data: str) -> None:
    vm = VM(data)
    for x in 1, 2:
        match vm.reset().send(x).get():
            case [ans]:
                print(ans)
            case other:
                raise Exception(repr(other))


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
