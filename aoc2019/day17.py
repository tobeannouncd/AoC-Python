from io import StringIO
from string import ascii_uppercase

from aoc2019.intcode import VM
from lattice import Point, from_str

DIRS = {
    'v': Point(0, 1),
    '<': Point(-1, 0),
    '>': Point(1, 0),
    '^': Point(0, -1)
}

def solve(data: str) -> None:
    pc = VM(data)
    
    o = StringIO()
    next(pc.ascii(out=o), None)

    scaffold = set()
    pos, facing = None, None
    for pt, val in from_str(o.getvalue()):
        if val == '#':
            scaffold.add(pt)
        elif (x := DIRS.get(val)):
            pos = pt
            facing = x
    assert pos and facing
    
    intersections = (x for x in scaffold if all(a in scaffold for a in x.adjacent()))
    print(sum(x*y for x,y in intersections))

    steps = []
    while True:
        if facing.rot_ccw() + pos in scaffold:
            steps.append("L")
            facing = facing.rot_ccw()
        elif facing.rot_cw() + pos in scaffold:
            steps.append("R")
            facing = facing.rot_cw()
        else:
            break
        n = 0
        while facing + pos in scaffold:
            n += 1
            pos += facing
        steps.append(str(n))
    path = ','.join(steps)
    
    routines = []
    for char in "ABC":
        steps = path.split(',')
        subs = set()
        for i, x in enumerate(steps[:-1]):
            if x not in "LR":
                continue
            for j, y in enumerate(steps[i+1:], i+1):
                if y in "ABC":
                    break
                elif y in "LR":
                    continue
                s = ','.join(steps[i:j+1])
                if len(s) > 20:
                    break
                subs.add(s)
        routines.append(s := min(subs, key=lambda x: len(path.replace(x, char))))
        path = path.replace(s, char)
    
    inp = StringIO('\n'.join((path, *routines, 'n')))
    pc.reset()
    pc[0] = 2
    print(next(pc.ascii(inp)))
        



if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
