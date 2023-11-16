

def solve(data) -> None:
    pos, depth = 0, 0
    for line in data.splitlines():
        match line.split():
            case ["forward", x]:
                pos += int(x)
            case ["down", x]:
                depth += int(x)
            case ["up", x]:
                depth -= int(x)
    print(pos*depth)

    pos, depth, aim = 0, 0, 0
    for line in data.splitlines():
        match line.split():
            case ["forward", x]:
                pos += int(x)
                depth += aim*int(x)
            case ["down", x]:
                aim += int(x)
            case ["up", x]:
                aim -= int(x)
    print(pos*depth)



def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
