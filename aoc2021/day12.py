from collections import defaultdict
from functools import cache


def solve(data) -> None:
    connections: defaultdict[str, set[str]] = defaultdict(set)
    for line in data.splitlines():
        a, b = line.split('-')
        connections[a].add(b)
        connections[b].add(a)

    @cache
    def count_paths(path: tuple[str, ...], part=1) -> int:
        total = 0
        for destination in connections[path[-1]]:
            if destination == 'end':
                total += 1
                continue
            elif destination == 'start':
                continue
            elif destination.islower() and destination in path:
                if part == 1:
                    continue
                elif part == 2:
                    total += count_paths(path + (destination,), 1)
            else:
                total += count_paths(path + (destination, ), part)
        return total

    print(count_paths(('start', )))
    print(count_paths(('start', ), 2))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
