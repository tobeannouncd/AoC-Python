from dataclasses import dataclass
from functools import cache
from itertools import count, cycle, product

from utils import *


def sim(a, b, max_score=1000):
    positions = [a, b]
    rolls = 0
    die = 1
    scores = [0, 0]
    for i in cycle((0, 1)):
        move = 0
        for _ in range(3):
            rolls += 1
            move += die
            die += 1
            if die == 101:
                die = 1
        positions[i] += move % 10
        if positions[i] > 10:
            positions[i] -= 10
        scores[i] += positions[i]
        if scores[i] >= max_score:
            break
    return rolls, scores

@cache
def wins_losses(pos_cur, pos_other, score_cur, score_other):
    wins, losses = 0, 0
    for rolls in product(range(1, 4), repeat=3):
        roll = sum(rolls)
        new_pos = pos_cur + roll
        if new_pos > 10:
            new_pos -= 10
        new_score = score_cur + new_pos
        if new_score >= 21:
            wins += 1
            continue
        l, w = wins_losses(pos_other, new_pos, score_other, new_score)
        wins += w
        losses += l
    return wins, losses


def solve(data: str) -> None:
    _, a, _, b = to_ints(data)
    rolls, scores = sim(a, b)
    print(rolls*min(scores))

    w, l = wins_losses(a, b, 0, 0)
    print(max(w,l))




def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
