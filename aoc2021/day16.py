from math import prod
from utils import *

OPS = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}


class Packet:

    def __init__(self, version: int, type_id: int) -> None:
        self.version = version
        self.type_id = type_id
        self._val = None
        self.subpackets: list[Packet] = []

    @property
    def val(self):
        if self._val is None:
            f = OPS[self.type_id]
            self._val = f([s.val for s in self.subpackets])
        return self._val

    @val.setter
    def val(self, x):
        self._val = x


LITERAL = 4


def get_packet(b: str) -> tuple[Packet, str]:
    version = int(b[:3], 2)
    type_id = int(b[3:6], 2)
    p = Packet(version, type_id)
    if type_id == LITERAL:
        val, b = parse_literal(b[6:])
        p.val = val
        return p, b
    length_id = int(b[6], 2)
    if length_id == 0:
        n = int(b[7:22], 2)
        b_, b = b[22:22 + n], b[22 + n:]
        while b_:
            s, b_ = get_packet(b_)
            p.subpackets.append(s)
    else:
        n = int(b[7:18], 2)
        b = b[18:]
        for _ in range(n):
            s, b = get_packet(b)
            p.subpackets.append(s)
    return p, b


def parse_literal(b: str) -> tuple[int, str]:
    out = ''
    while True:
        x, b = b[:5], b[5:]
        out += x[1:]
        if x[0] == '0':
            break
    return int(out, 2), b


def solve(data: str) -> None:
    b = ''
    for ch in data:
        n = int(ch, 16)
        b += f'{n:04b}'
    p, _ = get_packet(b)
    ans = 0
    stack = [p]
    while stack:
        cur = stack.pop()
        ans += cur.version
        stack.extend(cur.subpackets)
    print(ans)
    print(p.val)


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
