from hashlib import md5
from itertools import count

def find_password(secret_key: str, leading_zeros: int) -> int:
    for n in count():
        s = f'{secret_key}{n}'
        h = md5(s.encode()).hexdigest()
        if h.startswith('0'*leading_zeros):
            return n
    return -1


def solve(data) -> None:
    print(find_password(data.strip(), 5))
    print(find_password(data.strip(), 6))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
