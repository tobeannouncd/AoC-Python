from itertools import combinations, permutations, product

import numpy as np

from parsing import integers

ROTS = []
for x, y in product((1,-1), repeat=2):
    for i, j in permutations(range(3), 2):
        a, b = [0]*3, [0]*3
        a[i], b[j] = x, y
        ROTS.append(np.array([a, b, np.cross(a, b)]))

def invar(a, b) -> tuple[int,...]:
    return tuple(sorted(abs(aa-bb) for aa,bb in zip(a, b)))

def disp(a, b) -> tuple[int,...]:
    x = tuple(aa-bb for aa,bb in zip(a, b))
    y = tuple(bb-aa for aa,bb in zip(a, b))
    return max(x, y)

def manhattan(a, b):
    return sum(abs(aa-bb) for aa,bb in zip(a, b))


def solve(data: str) -> None:
    scanners = {}
    invars = {}
    for p in data.split("\n\n"):
        header, *rem = p.splitlines()
        n = int(header.split()[2])
        scanners[n] = np.array([integers(x) for x in rem])
        invars[n] = set()
        for a, b in combinations(scanners[n], 2):
            invars[n].add(invar(a, b))

    aligned = {next(k for k in scanners)}
    unaligned = set(scanners) - aligned
    offsets = {a:np.zeros(3, int) for a in aligned}
    while unaligned:
        a, u = next((a,u) for a,u in product(aligned, unaligned) if len(invars[a] & invars[u]) >= 66)
        tgt = {disp(x,y) for x,y in combinations(scanners[a], 2)}
        rot = None
        for r in ROTS:
            m = scanners[u] @ r
            cur = {disp(x,y) for x,y in combinations(m, 2)}
            if len(cur & tgt) >= 66:
                rot = m
                break
        else:
            raise Exception('no valid rotations')

        tgt = {tuple(x) for x in scanners[a]}
        for fixed, moving in product(scanners[a], rot):
            offset = fixed - moving
            m = rot + offset
            cur = {tuple(x) for x in m}
            if len(tgt & cur) >= 12:
                scanners[u] = m
                offsets[u] = offset
                aligned.add(u)
                unaligned.remove(u)
                break
        else:
            raise Exception('could not align')
    
    pts = set()
    for s in scanners.values():
        pts.update(map(tuple, s))
    print(len(pts))

    print(max(
        manhattan(a, b)
        for a, b in combinations(offsets.values(), 2)
    ))





if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
