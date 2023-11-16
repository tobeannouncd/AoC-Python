from parsing import integers


def is_winner(board: list[list[int]]) -> bool:
    if any(all(x == -1 for x in row) for row in board):
        return True
    return any(all(x == -1 for x in col) for col in zip(*board))


def solve(data) -> None:
    a, *b = data.split("\n\n")
    nums = integers(a)
    boards = []
    for line in b:
        boards.append([integers(row) for row in line.splitlines()])
    winners = set()
    for n in nums:
        for i, board in enumerate(boards):
            for row in board:
                for j, val in enumerate(row):
                    if val == n:
                        row[j] = -1
            if i not in winners and is_winner(board):
                if not winners or len(winners) + 1 == len(boards):
                    print(n * sum(sum(x for x in row if x != -1) for row in board))
                winners.add(i)


def main():
    from aocd import data

    solve(data)


if __name__ == "__main__":
    main()
