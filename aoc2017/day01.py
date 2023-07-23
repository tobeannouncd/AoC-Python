def solve(data: str) -> None:
    digits = [int(x) for x in data.strip()]

    for i in 1, len(digits) // 2:
        ans = 0
        for a, b in zip(digits, digits[i:] + digits[:i]):
            if a == b:
                ans += a
        print(ans)


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
