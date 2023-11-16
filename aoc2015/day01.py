def solve(data: str) -> None:
    key = {'(': 1, ')': -1}
    floor = 0
    history = [floor]
    for char in data.strip():
        floor += key[char]
        history.append(floor)
    print(floor)
    print(history.index(-1))


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
