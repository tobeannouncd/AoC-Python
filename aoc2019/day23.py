from aoc2019.intcode import VM


class PC(VM):
    @property
    def waiting(self):
        return not self._inp


def solve(data: str) -> None:
    pcs = [PC(data, i) for i in range(50)]
    NIC = None
    last_y_sent = None
    while True:
        idle = True
        for pc in pcs:
            if pc.waiting:
                pc.send(-1)
            while (i := next(pc)) is not None:
                idle = False
                x, y = pc.get(2)
                if i == 255:
                    if NIC is None:
                        print(y)
                    NIC = x, y
                else:
                    pcs[i].send(x, y)
        if idle and NIC:
            if NIC[1] == last_y_sent:
                print(NIC[1])
                break
            pcs[0].send(*NIC)
            last_y_sent = NIC[1]


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
