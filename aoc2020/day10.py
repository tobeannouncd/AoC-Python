from collections import Counter
from parsing import integers

def solve(data) -> None:
    adapters = sorted(integers(data))
    gaps = Counter()
    for a,b in zip([0]+adapters, adapters + [adapters[-1]+3]):
        gaps[b-a] += 1
    print(gaps[1] * gaps[3])
    ways = Counter()
    ways[0] = 1
    for a in adapters:
        for x in range(a-3,a):
            ways[a] += ways[x]
    print(ways[adapters[-1]])


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
