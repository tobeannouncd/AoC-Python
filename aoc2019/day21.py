from io import StringIO
from sys import stdout
from aocd import data
from intcode import *
from utils import *


def run(lines: list[str], debug=False):
    droid = Intcode(data)
    inp = StringIO('\n'.join(lines))
    out = stdout if debug else StringIO()
    return droid.ascii(inp, out)

part_one = [
    'OR A J',
    'AND B J',
    'AND C J',
    'NOT J J',
    'AND D J',
    'WALK',
]

print(run(part_one))

part_two = [
    'OR A J',
    'AND B J',
    'AND C J',
    'NOT J J',
    'AND D J',
    'OR E T',
    'OR H T',
    'AND T J',
    'RUN',
]

print(run(part_two))