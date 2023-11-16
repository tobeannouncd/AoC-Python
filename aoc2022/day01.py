from heapq import nlargest


def solve(data: str):
    elves = [sum(int(x) for x in p.splitlines()) for p in data.split("\n\n")]
    for x in 1, 3:
        print(sum(nlargest(x, elves)))


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
