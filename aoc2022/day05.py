from pprint import pprint


def solve(data: str) -> None:
    data, steps = data.split("\n\n")
    stacks = {}
    for col in zip(*data.splitlines()):
        if col and col[-1].isdigit():
            stk = ''.join(col[:-1]).strip()
            stacks[int(col[-1])] = stk[::-1]

    for part in 1, 2:
        crates = {k:list(v) for k,v in stacks.items()}
        for line in steps.splitlines():
            _, n, _, i, _, j = line.split()
            n, i, j = map(int, [n, i, j])
            tmp = crates[i][-n:]
            crates[i][:] = crates[i][:-n]
            crates[j].extend(tmp if part == 2 else reversed(tmp))
        print(''.join(v[-1] for k,v in sorted(crates.items())))

if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
