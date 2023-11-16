import numpy as np


@np.vectorize
def turn_off(x):
    return max(0, x-1)

def solve(data: str) -> None:
    for part in 1, 2:
        grid = np.zeros((1000,1000), int)
        for line in data.splitlines():
            match line.split():
                case [_, "on", lo, _, hi]:
                    s = get_slice(lo, hi)
                    if part == 1:
                        grid[s] = 1
                    else:
                        grid[s] += 1
                case [_, lo, _, hi]:
                    s = get_slice(lo, hi)
                    if part == 1:
                        grid[s] ^= 1
                    else:
                        grid[s] += 2
                case [_, "off", lo, _, hi]:
                    s = get_slice(lo, hi)
                    if part == 1:
                        grid[s] = 0
                    else:
                        grid[s] = turn_off(grid[s])
        print(grid.sum())


def get_slice(lo, hi):
    i,j = map(int, lo.split(','))
    ii,jj = map(int, hi.split(','))
    s = slice(i, ii+1), slice(j, jj+1)
    return s
                



if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
