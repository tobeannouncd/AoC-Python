from itertools import product
from aocd import data
from utils import *
from intcode import *


def is_pulled(x, y):
    i = Intcode(data)
    i.write(x)
    i.write(y)
    return bool(i.read(1)[0])


print(sum(1 for x, y in product(range(50), repeat=2) if is_pulled(x, y)))

x, y = 0, 99
while not is_pulled(x, y):
    x += 1
    while not is_pulled(x + 99, y - 99):
        y += 1
print(10_000 * x + y - 99)
