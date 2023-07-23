from itertools import permutations


def solve(data: str) -> None:
    spreadsheet = [[int(x) for x in y.split()] for y in data.splitlines()]

    checksum = 0
    for row in spreadsheet:
        checksum += max(row) - min(row)
    print(checksum)

    checksum = 0
    for row in spreadsheet:
        a, b = next((a, b) for a, b in permutations(row, 2) if not a % b)
        checksum += a // b
    print(checksum)


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
