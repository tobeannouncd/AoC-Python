from typing import Optional

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

SYNTAX_VALS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

COMPLETION_VALS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def judge(line: str) -> int | str:
    completion_str = ''
    for char in line:
        if char in PAIRS:
            completion_str = PAIRS[char] + completion_str
        elif completion_str.startswith(char):
            completion_str = completion_str[1:]
        else:
            return SYNTAX_VALS[char]
    return completion_str


def solve(data) -> None:
    incomplete = []
    syntax_score = 0
    for line in data.splitlines():
        x = judge(line)
        if isinstance(x, int):
            syntax_score += x
        else:
            incomplete.append(x)
    print(syntax_score)

    completion_scores = []
    for s in incomplete:
        score = 0
        for ch in s:
            score = 5*score + COMPLETION_VALS[ch]
        completion_scores.append(score)
    completion_scores.sort()
    N = len(completion_scores)
    print(completion_scores[N//2])
    

def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
