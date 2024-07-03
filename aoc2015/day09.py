from collections import defaultdict
import re
from search import dijkstra

def solve(data: str) -> None:
    edges: defaultdict[str, dict[str, int]] = defaultdict(dict)
    for line in data.splitlines():
        if (m := re.match(r"(.+) to (.+) = (\d+)", line)) is not None:
            a, b, n = m.groups()
            edges[a][b] = edges[b][a] = int(n)

    starts = ((k,frozenset()) for k in edges)
    def neighbors(x):
        here, prev = x
        for y in edges[here]:
            if y not in prev:
                yield y, prev | {here}
    cost = lambda a,b: edges[a[0]][b[0]]
    costs = (c for c, (_,x) in dijkstra(starts, neighbors, cost, True)
             if len(x) + 1 == len(edges)
             )
    print(next(costs))
    *_, x = costs
    print(x)


if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
