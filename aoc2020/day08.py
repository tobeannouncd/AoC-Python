from enum import Enum


class Op(Enum):
    Acc = 'acc'
    Nop = 'nop'
    Jmp = 'jmp'

def parseLine(line: str) -> tuple[Op, int]:
    a, b = line.split()
    return Op(a), int(b)

def solve(data: str) -> None:
    program = list(map(parseLine, data.splitlines()))
    _, acc = loops(program)
    print(acc)
    for i, (o, x) in enumerate(program):
        if o is Op.Acc:
            continue
        prog = list(program)
        if o is Op.Nop:
            prog[i] = Op.Jmp, x
        elif o is Op.Jmp:
            prog[i] = Op.Nop, x
        looped, acc = loops(prog)
        if not looped:
            print(acc)
            break

def loops(program) -> tuple[bool, int]:
    accumulator = 0
    pointer = 0
    N = len(program)
    history = set()
    while pointer in range(N):
        if pointer in history:
            return True, accumulator
        history.add(pointer)
        match program[pointer]:
            case Op.Acc, x:
                accumulator += x
                pointer += 1
            case Op.Nop, _:
                pointer += 1
            case Op.Jmp, x:
                pointer += x
    return False, accumulator

def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
