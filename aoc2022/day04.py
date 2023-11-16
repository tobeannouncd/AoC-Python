def solve(data: str) -> None:
    contain = 0
    overlap = 0
    for line in data.splitlines():
        (a, b), (x, y) = ((int(x) for x in y.split("-")) for y in line.split(","))
        if a <= x and y <= b or x <= a and b <= y:
            contain += 1
            overlap += 1
        elif a <= x <= b or x <= a <= y:
            overlap += 1
    print(contain)
    print(overlap)


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
