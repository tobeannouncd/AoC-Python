from itertools import product
from typing import Iterator, Mapping
from utils import *


def window(p: Point) -> Iterator[Point]:
    for y in range(p.y - 1, p.y + 2):
        for x in range(p.x - 1, p.x + 2):
            yield Point(x, y)


TBL = str.maketrans('#.', '10')


def solve(data: str) -> None:
    algorithm, data = data.split('\n\n')
    image = '.', to_grid(data)
    for _ in range(2):
        image = enhance(algorithm, image)
    print(sum(1 for v in image[1].values() if v == '#'))

    for _ in range(48):
        image = enhance(algorithm, image)
    print(sum(1 for v in image[1].values() if v == '#'))


def enhance(algorithm: str, image: tuple[str, Mapping[Point, str]]):
    default, grid = image
    p_min, p_max = min(grid), max(grid)
    out = {}
    for x, y in product(range(p_min.x - 1, p_max.x + 2),
                        range(p_min.y - 1, p_max.y + 2)):
        p = Point(x, y)
        s = ''.join(grid.get(w, default) for w in window(p))
        i = int(s.translate(TBL), 2)
        out[p] = algorithm[i]
    d = '#' if default == '.' else '.'
    return d, out


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
