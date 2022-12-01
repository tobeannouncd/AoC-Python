import re
from typing import Optional


def parse_passport(s: str) -> Optional[dict]:
    p = {}
    for line in s.splitlines():
        for part in line.split():
            k, v = part.split(':')
            p[k] = v
    if all(field in p for field in 'byr,iyr,eyr,hgt,hcl,ecl,pid'.split(',')):
        return p


def is_valid(p: dict[str, str]) -> bool:
    try:
        byr = p.get('byr', '')
        assert re.fullmatch(r'19[2-9]\d|200[0-2]', byr)
        iyr = p.get('iyr', '')
        assert re.fullmatch(r'201\d|2020', iyr)
        eyr = p.get('eyr', '')
        assert re.fullmatch(r'202\d|2030', eyr)
        hgt = p.get('hgt','')
        assert re.fullmatch(r'(?:1[5-8]\d|19[0-3])cm|(?:59|6\d|7[0-6])in', hgt)
        hcl = p.get('hcl', '')
        assert re.fullmatch(r'#[0-9a-f]{6}', hcl)
        ecl = p.get('ecl','')
        assert re.fullmatch(r'amb|blu|brn|gry|grn|hzl|oth', ecl)
        pid = p.get('pid', '')
        assert re.fullmatch(r'\d{9}', pid)
        return True
    except AssertionError:
        return False


def solve(data: str) -> None:
    complete = []
    for group in data.split('\n\n'):
        p = parse_passport(group)
        if p:
            complete.append(p)
    print(len(complete))
    print(sum(1 for _ in filter(is_valid, complete)))

def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
