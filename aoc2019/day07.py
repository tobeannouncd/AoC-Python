from itertools import cycle, permutations

from aocd import data

from intcode import *


def run_once(phases):
    amps = setup_amps(phases)
    signal = 0
    for a in amps:
        a.write(signal)
        signal, = a.read(1)
    return signal


def setup_amps(phases):
    amps = []
    for p in phases:
        amp = Intcode(data)
        amp.write(p)
        amps.append(amp)
    return amps


def loop(phases) -> int:
    amps = setup_amps(phases)
    signal = 0
    for i in cycle(range(len(amps))):
        amp = amps[i]
        amp.write(signal)
        x = amp.read(1)
        if not x:
            break
        signal, = x
    return signal


print(max(run_once(p) for p in permutations(range(5))))
print(max(loop(p) for p in permutations(range(5, 10))))
