
BEATS = dict(zip("ABC", "BCA"))


def score(theirs: str, yours: str) -> int:
    s = "ABC".index(yours) + 1
    if theirs == yours:
        s += 3
    elif BEATS[theirs] == yours:
        s += 6
    return s

def strat_a(theirs: str, yours: str) -> tuple[str, str]:
    t = str.maketrans("XYZ", "ABC")
    return theirs, yours.translate(t)

def strat_b(theirs: str, yours: str):
    if yours == 'X':
        x = next(k for k,v in BEATS.items() if v == theirs)
    elif yours == 'Y':
        x = theirs
    elif yours == 'Z':
        x = BEATS[theirs]
    else:
        raise ValueError(f"unknown throw: {yours}")
    return theirs, x

def solve(data: str) -> None:
    throws = [x.split() for x in data.splitlines()]
    for strat in strat_a, strat_b:
        print(sum(score(*strat(*throw)) for throw in throws))



if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
