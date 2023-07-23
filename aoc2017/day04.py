def solve(data: str) -> None:
    passphrases = data.splitlines()

    for part in 1, 2:
        n_valid = 0
        for passphrase in passphrases:
            words = passphrase.split()
            unique = set(words) if part == 1 else set(tuple(sorted(x)) for x in words)
            if len(words) == len(unique):
                n_valid += 1
        print(n_valid)


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
