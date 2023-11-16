from io import StringIO
from aoc2019.intcode import VM


def solve(data: str) -> None:
    script_a = """
OR A J
AND B J
AND C J
NOT J J
AND D J
WALK""".strip()
    
    script_b = """
OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN""".strip()
    
    droid = VM(data)
    for s in script_a, script_b:
        print(next(droid.reset().ascii(StringIO(s))))


if __name__ == '__main__':
    from aocd import data

    assert isinstance(data, str)
    solve(data)
