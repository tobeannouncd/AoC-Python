from utils import *

DIRS = {
    '<': Point(-1, 0),
    '>': Point(1, 0),
    'v': Point(0, 1),
    '^': Point(0, -1),
}

def solve(data: str) -> None:
    print(part_one(data))
    print(part_two(data))

def part_one(data):
    santa = Point(0, 0)
    houses = {santa}
    for char in data.strip():
        d = DIRS[char]
        santa += d
        houses.add(santa)
    return len(houses)

def part_two(data):
    santa = Point(0, 0)
    robo = Point(0, 0)
    houses = {santa}
    for i, char in enumerate(data.strip()):
        d = DIRS[char]
        if i % 2:
            robo += d
            houses.add(robo)
        else:
            santa += d
            houses.add(santa)
    return len(houses)


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
