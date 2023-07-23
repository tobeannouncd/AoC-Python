from lattice import Point


def solve(data: str) -> None:
    square = int(data)

    pos, n = Point(0, 0), 1
    while n * n < square:
        pos += Point(1, 1)
        n += 2
    val = n * n
    facing = Point(-1, 0)
    while val > square:
        val -= 1
        pos += facing
        if abs(pos.x) == abs(pos.y):
            facing = facing.rot_cw()
    print(abs(pos))

    pos = Point(0, 0)
    facing = Point(1, 0)
    grid = {pos: 1}
    while grid[pos] < square:
        pos += facing
        if pos + facing.rot_ccw() not in grid:
            facing = facing.rot_ccw()
        grid[pos] = sum(grid.get(a, 0) for a in pos.adjacent(8))
    print(grid[pos])


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
