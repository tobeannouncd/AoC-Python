from utils import split_paragraphs, to_ints


def solve(data: str) -> None:
    elves = list(map(to_ints, split_paragraphs(data)))
    weight = sorted(map(sum, elves))
    print(weight[-1])

    print(sum(weight[-3:]))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
