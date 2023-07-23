from io import StringIO
from aoc2019.intcode import VM
from lattice import from_str, Point

DIRS = dict(zip("<^v>", Point(0, 0).adjacent()))
LIMIT = 20

def solve(data: str) -> None:
    robot = VM(data)
    out = StringIO()
    next(robot.ascii(StringIO(), out), None)

    scaffold = dict(from_str(out.getvalue()))
    print(
        sum(
            pt.x * pt.y
            for pt, val in scaffold.items()
            if val == "#" and all(scaffold.get(a) == "#" for a in pt.adjacent(4))
        )
    )
    
    pos, facing = next((pt, DIRS[val]) for pt, val in scaffold.items() if val in DIRS)
    steps = []
    while True:
        if scaffold.get(pos + facing.rot_ccw()) == '#':
            steps.append("L")
            facing = facing.rot_ccw()
        elif scaffold.get(pos + facing.rot_cw()) == '#':
            steps.append("R")
            facing = facing.rot_cw()
        else:
            break
        n = 0
        while scaffold.get(pos+facing) == '#':
            n += 1
            pos += facing
        steps.append(str(n))
    path = ','.join(steps)
    
    routines = []
    for ch in "ABC":
        steps = path.split(',')
        replacements = set()
        for i, step in enumerate(steps):
            if step not in "RL":
                continue
            for j, end in enumerate(steps[i+1:], i+1):
                if end in "RL":
                    continue
                if not end.isdigit():
                    break
                repl = ','.join(steps[i:j+1])
                if len(repl) > LIMIT:
                    break
                replacements.add(repl)
        routine = min(replacements, key=lambda x: len(path.replace(x, ch)))
        routines.append(routine)
        path = path.replace(routine, ch)
    
    inp = [path, *routines, "n"]
    inp = StringIO("\n".join(inp))
    robot = VM(data)
    robot.memory[0] = 2
    print(next(robot.ascii(inp, StringIO())))


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
