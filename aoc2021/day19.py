from functools import cache, partial
from itertools import combinations, permutations, product
from typing import Iterator
from utils import *

P = list[int] | tuple[int, int, int]


def orientations(s: set[P]) -> Iterator[set[P]]:
    for o in transform_matrices():
        yield set(map(partial(rotate_point, o), s))


def rotate_point(transformation_mat: tuple[P, P, P], pt: P) -> P:
    out = []
    for row in transformation_mat:
        out.append(sum(a * b for a, b in zip(row, pt)))
    return tuple(out)


def transform_matrices() -> Iterator[tuple[P, P, P]]:
    for i, j in permutations(range(3), 2):
        for m, n in product((-1, 1), repeat=2):
            a = [0, 0, 0]
            a[i] = m
            b = [0, 0, 0]
            b[j] = n
            c = cross(a, b)
            yield a, b, c


def cross(a: P, b: P) -> list[int]:
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def alignments(fixed: set[P], moveable: set[P]) -> Iterator[set[P]]:
    for o in orientations(moveable):
        for f, m in product(fixed, o):
            yield {move_point(pt, f, m) for pt in o}


def move_point(pt: P, end: P, start: P) -> P:
    diff = [e - s for e, s in zip(end, start)]
    return tuple(p + d for p, d in zip(pt, diff))


def invariant(a: P, b: P) -> P:
    return tuple(sorted(abs(aa - bb) for aa, bb in zip(a, b)))


def set_invariants(s: set[P]) -> set[P]:
    out = set()
    for a, b in combinations(s, 2):
        out.add(invariant(a, b))
    return out


def solve(data: str):
    visible: dict[int, set[P]] = {}
    for i, group in enumerate(data.split('\n\n')):
        visible[i] = set()
        for line in group.splitlines()[1:]:
            pt = tuple(map(int, line.split(',')))
            visible[i].add(pt)
    aligned = {0: visible[0]}
    invars = {i: set_invariants(visible[i]) for i in visible}

    @cache
    def score(pair: tuple[int, int]):
        a, b = pair
        return len(invars[a].intersection(invars[b]))

    unaligned = set(visible).difference(aligned)
    while unaligned:
        a, u = max(product(aligned, unaligned), key=score)
        for alignment in alignments(aligned[a], visible[u]):
            common = alignment & aligned[a]
            if len(common) >= 12:
                aligned[u] = alignment
                break
        unaligned.remove(u)

    print(len(set.union(*aligned.values())))
    print(
        max(
            manhattan(a, b)
            for a, b in combinations(set.union(*aligned.values()), 2)))


def manhattan(a: P, b: P) -> int:
    return sum(abs(aa - bb) for aa, bb in zip(a, b))


if __name__ == '__main__':
    from aocd import data
    solve(data)
