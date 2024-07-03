from itertools import combinations_with_replacement, pairwise

import numpy as np
import numpy.typing as npt

def combos(k, n):
    for markers in combinations_with_replacement(range(n+1), k-1):
        lst = [b-a for a,b in pairwise((0, *markers, 100))]
        yield lst

def solve(data: str) -> None:
    ingredients = {}
    for line in data.splitlines():
        name, x = line.split(':')
        props = []
        for p in x.split(','):
            props.append(int(p.split()[-1]))
        ingredients[name] = np.array(props)

    cookies = []
    for combo in combos(len(ingredients), 100):
        cookies.append(sum(n*i for n, i in zip(combo, ingredients.values())))
    print(max(
        np.prod(np.fmax(0, c[:-1]))
        for c in cookies
    ))
    print(max(
        np.prod(np.fmax(0, c[:-1]))
        for c in cookies
        if c[-1] == 500
    ))

if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)

