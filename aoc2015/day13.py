from collections import defaultdict
from itertools import pairwise, permutations
import re


def solve(data: str) -> None:
    edges = defaultdict(dict)
    for line in data.splitlines():
        m = re.match(r"(.+) would (gain|lose) (\d+) happiness units? by sitting next to (.+)\.", line)
        if not m: raise ValueError(line)
        a, gl, n, b = m.groups()
        n = int(n) * (1 if gl == 'gain' else -1)
        edges[a][b] = n

    for _ in range(2):
        best = float('-inf')
        for perm in permutations(edges):
            h = sum(edges[a][b] + edges[b][a] for a, b in pairwise(perm + perm[:1]))
            best = max(best, h)
        print(best)
        for x in list(edges):
            edges[x][''] = edges[''][x] = 0




if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
