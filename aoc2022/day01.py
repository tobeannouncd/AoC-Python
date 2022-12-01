from utils import split_paragraphs, to_ints


def solve(data: str) -> None:
    elves = list(map(to_ints, split_paragraphs(data)))
    total_weight = sorted(map(sum, elves))
    print(total_weight[-1])

    print(sum(total_weight[-3:]))


if __name__ == "__main__":
    from aocd import data

    solve(data)
