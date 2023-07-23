from math import lcm
from utils import ints, paragraphs

class Monkey:
    def __init__(self, s: str):
        monkey, starting_items, operation, test, true_op, false_op = s.splitlines()
        self.id, = ints(monkey)
        self.items = ints(starting_items)
        self.operation = operation.split('= ')[1]
        self.div, = ints(test)
        self.true_target, = ints(true_op)
        self.false_target, = ints(false_op)
        self.inspected = 0
    
    def round(self, relieved, mod):
        out = []
        for old in self.items:
            self.inspected += 1
            new = eval(self.operation)
            if relieved:
                new //= 3
            new %= mod
            if not new % self.div:
                target = self.true_target
            else:
                target = self.false_target
            out.append((target, new))
        self.items.clear()
        return out


def solve(data: str) -> None:
    run(data, 20, True)
    run(data, 10_000, False)

def run(data, rounds, relieved):
    monkeys = []
    for p in paragraphs(data):
        m = Monkey(p)
        monkeys.append(m)
    mod = 1
    for m in monkeys:
        mod = lcm(mod, m.div)
    for _ in range(rounds):
        for m in monkeys:
            for target, val in m.round(relieved, mod):
                monkeys[target].items.append(val)
    s = sorted(m.inspected for m in monkeys)
    print(s[-2]*s[-1])
    


if __name__ == "__main__":
    from aocd import data

    solve(data)
    sample = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    # solve(sample)
