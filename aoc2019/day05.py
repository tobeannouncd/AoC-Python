from intcode import Intcode, parse
from aocd import data


def solve(val, part_two=False):
    pc = Intcode(data)
    pc.write(val)
    out = pc.read()
    if part_two:
        assert len(out) == 1
    else:
        assert all(not x for x in out[:-1])
    return out[-1]


print(solve(1))
print(solve(5, True))
