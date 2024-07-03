import re

from iter_extra import iterate, windows
from bench import benchmark

def valid(password: str) -> bool:
    return (all(x not in password for x in "iol") and
            any(a+2 == b+1 == c for a,b,c in windows(list(map(ord, password)), 3)) and
            len(set(re.findall(r"(.)\1", password))) > 1)

@benchmark()
def solve(data: str) -> None:
    passwords = filter(valid, iterate(next_str, data.strip()))
    for i in range(2):
        print(next(passwords))

def next_str(s: str) -> str:
    if s.endswith('z'):
        return next_str(s[:-1]) + 'a'
    return s[:-1] + chr(1 + ord(s[-1]))



if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
