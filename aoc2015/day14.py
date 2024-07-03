from collections import Counter
from functools import partial
import re

def fly(time: int, reindeer: tuple[int,int,int]) -> int:
    speed, endurance, rest = reindeer
    n, t = divmod(time, endurance + rest)
    return speed * (n * endurance + min(endurance, t))


def solve(data: str) -> None:
    reindeer = {}
    for line in data.splitlines():
        m = re.match(r"(.+) can fly (\d+) km/s for (\d+) seconds?, but then "
                     r"must rest for (\d+) seconds?\.", line)
        if not m: raise ValueError(line)
        name, *rest = m.groups()
        reindeer[name] = tuple(map(int, rest))
    print(max(map(partial(fly, 2503), reindeer.values())))

    score = Counter()
    for t in range(1, 2504):
        lst = [(k, fly(t, v)) for k, v in reindeer.items()]
        mx = max(x[1] for x in lst)
        for k,v in lst:
            if v == mx:
                score[k] += 1
    print(max(score.values()))



if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
