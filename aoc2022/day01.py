from utils import paragraphs, ints


def solve(data: str) -> None:
    elves = map(ints, paragraphs(data))
    total_weight = sorted(map(sum, elves))
    print(total_weight[-1])

    print(sum(total_weight[-3:]))


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
