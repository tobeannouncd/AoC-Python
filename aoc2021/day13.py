

from lattice import Point, to_str
from parsing import integers


def solve(data) -> None:
    a, instructions = data.split('\n\n')
    dots = {Point(*integers(line)) for line in a.splitlines()}
    instructions = instructions.splitlines()
    fold_paper(dots, instructions[0])
    print(len(dots))

    for inst in instructions[1:]:
        fold_paper(dots,inst)
    grid = {d:'#' for d in dots}
    print(to_str(grid))

def fold_paper(dots, instruction):
    match instruction.split()[-1].split('='):
        case ['y', n]:
            n = int(n)
            for d in dots.copy():
                if d.y > n:
                    dots.remove(d)
                    dots.add(Point(d.x, 2*n-d.y))
        case ['x', n]:
            n = int(n)
            for d in dots.copy():
                if d.x > n:
                    dots.remove(d)
                    dots.add(Point(2*n-d.x, d.y))
    


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
