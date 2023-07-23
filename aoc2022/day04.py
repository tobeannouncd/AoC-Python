import utils

def solve(data: str) -> None:
    ans = 0
    ans2 = 0
    for line in data.splitlines():
        a, b, c, d = utils.ints(line)
        ar = set(range(a,b+1))
        br = set(range(c,d+1))
        if ar >= br or ar <= br:
            ans += 1
        if ar & br:
            ans2 += 1
    print(ans)
    print(ans2)


if __name__ == "__main__":
    from aocd import data

    solve(data)
