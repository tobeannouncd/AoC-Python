from itertools import permutations
from typing import Collection
"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 """

DIGIT_SEGS = list(
    map(set, [
        'abcefg',
        'cf',
        'acdeg',
        'acdfg',
        'bcdf',
        'abdfg',
        'abdefg',
        'acf',
        'abcdefg',
        'abcdfg',
    ]))


def decode(digits: Collection[str]):
    for p in permutations('abcdefg'):
        tbl = str.maketrans('abcdefg', ''.join(p))
        if all(set(d.translate(tbl)) in DIGIT_SEGS for d in digits):
            return tbl


def solve(data) -> None:
    ans = 0
    for line in data.splitlines():
        _, o = line.split(' | ')
        for digit in o.split():
            if len(digit) in (2, 4, 3, 7):
                ans += 1
    print(ans)

    out = 0
    for line in data.splitlines():
        d, o = line.split(' | ')
        digits = d.split()
        tbl = decode(digits)
        assert tbl is not None
        val = 0
        for x in o.split():
            dig = x.translate(tbl)
            n = DIGIT_SEGS.index(set(dig))
            val = 10 * val + n
        out += val
    print(out)


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
