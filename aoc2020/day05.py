def solve(data: str) -> None:
    seats = make_seats(data)
    print(max(seats))
    print(missing_seat(seats))


def missing_seat(seats: list[int]):
    seats.sort()
    for a, b in zip(seats, seats[1:]):
        if a + 1 != b:
            return a + 1


def make_seats(data: str):
    seats: list[int] = []
    tbl = str.maketrans('FBLR', '0101')
    for line in data.splitlines():
        seats.append(int(line.translate(tbl), 2))
    return seats


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
