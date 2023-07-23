def solve(data: str) -> None:
    ans = 0
    for rucksack in data.splitlines():
        n = len(rucksack)
        front = rucksack[:n//2]
        back = rucksack[n//2:]
        common = set(front).intersection(back)
        assert len(common) == 1
        ans += sum(map(priority, common))
    print(ans)
    N = len(data.splitlines())
    ans = 0
    for i in range(0,N,3):
        a, b, c = data.splitlines()[i:i+3]
        common = set(a).intersection(b,c)
        assert len(common) == 1
        ans += sum(map(priority, common))
    print(ans)

def priority(letter: str):
    if letter.islower():
        return ord(letter)-ord('a')+1
    else:
        return ord(letter) - ord('A') + 27


if __name__ == "__main__":
    from aocd import data

    solve(data)
