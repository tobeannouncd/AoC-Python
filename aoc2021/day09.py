from math import prod
from lattice import from_str


def solve(data) -> None:
    grid = {k: int(v) for k, v in from_str(data)}
    low_points = {
        k
        for k, v in grid.items()
        if all(v < grid.get(a, 9) for a in k.adjacent())
    }
    print(sum(grid[p] + 1 for p in low_points))

    basins = []
    for p in low_points:
        visited = set()
        stack = [p]
        while stack:
            p = stack.pop()
            visited.add(p)
            stack.extend(
                a for a in p.adjacent()
                if a not in visited.union(stack) and grid.get(a, 9) < 9)
        basins.append(len(visited))
    basins.sort()
    print(prod(basins[-3:]))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
