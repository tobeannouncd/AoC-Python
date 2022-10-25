from itertools import product

from aocd import data

from intcode import *



def alarm(noun, verb):
    pc = Intcode(data)
    pc[1] = noun
    pc[2] = verb
    pc.run()
    return pc[0]


print(alarm(12, 2))

for noun, verb in product(range(100), repeat=2):
    if alarm(noun, verb) == 19690720:
        print(100 * noun + verb)
        break
