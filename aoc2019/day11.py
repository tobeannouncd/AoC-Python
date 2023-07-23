from aoc2019.intcode import VM
from lattice import Point, to_str


def solve(data: str) -> None:
    for part in 1, 2:
        hull = {}
        pos = Point(0, 0)
        facing = Point(0, -1)
        if part == 2:
            hull[pos] = 1
        robot = VM(data)
        for _ in robot:
            robot.send(hull.get(pos, 0))
            hull[pos] = next(robot)
            if next(robot):
                facing = facing.rot_cw()
            else:
                facing = facing.rot_ccw()
            pos += facing
        if part == 1:
            print(len(hull))
        else:
            print(to_str(pt for pt, val in hull.items() if val == 1))


if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
