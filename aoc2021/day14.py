from collections import Counter



def solve(data) -> None:
    template, data = data.split('\n\n')
    rules = {}
    for line in data.splitlines():
        a, b = line.split(' -> ')
        rules[a] = b

    sim(template, rules, 10)
    sim(template, rules, 40)


def sim(template, rules, n):
    pair_count: Counter[str] = Counter()
    for a, b in zip(template, template[1:]):
        pair_count[a + b] += 1

    for _ in range(n):
        for (a, b), cnt in pair_count.copy().items():
            c = rules[a + b]
            pair_count[a + b] -= cnt
            pair_count[a + c] += cnt
            pair_count[c + b] += cnt
    elem_count = Counter()
    for (a, b), cnt in pair_count.items():
        elem_count[a] += cnt
        elem_count[b] += cnt
    elem_count[template[0]] += 1
    elem_count[template[-1]] += 1
    for k, v in elem_count.items():
        elem_count[k] = v // 2
    print(max(elem_count.values()) - min(elem_count.values()))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
