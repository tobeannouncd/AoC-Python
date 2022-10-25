from aocd import data
from intcode import *


def run(val: int):
    pc = Intcode(data)
    pc.write(val)
    out = pc.read()
    assert len(out) == 1
    print(out[0])


run(1)
run(2)