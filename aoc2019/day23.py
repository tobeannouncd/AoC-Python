from aocd import data
from intcode import *

network: list[Intcode] = []
for i in range(50):
    pc = Intcode(data)
    pc.write(i)
    network.append(pc)

nat = None
prev = None
while True:
    idle = True
    for pc in network:
        try:
            i, x, y = pc.read(3)
            idle = False
            if i == 255:
                if nat is None:
                    print(y)
                nat = x, y
                continue
            network[i].write(x)
            network[i].write(y)
        except NoInput:
            pc.write(-1)
    if idle and nat is not None:
        if nat[1] == prev:
            print(prev)
            break
        network[0].write(nat[0])
        network[0].write(nat[1])
        prev = nat[1]
