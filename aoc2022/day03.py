from iter_extra import chunks


def priority(s: str) -> int:
    if s.islower():
        return ord(s) - ord('a') + 1
    elif s.isupper():
        return ord(s) - ord('A') + 27
    else:
        raise ValueError

def solve(data: str) -> None:
    rucksacks = data.splitlines()

    ans = 0
    for r in rucksacks:
        i = len(r) // 2
        x = set(r[:i]).intersection(r[i:]).pop()
        ans += priority(x)
    print(ans)

    ans = 0
    for a, b, c in chunks(rucksacks, 3):
        x = set(a).intersection(b, c).pop()
        ans += priority(x)
    print(ans)

if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
