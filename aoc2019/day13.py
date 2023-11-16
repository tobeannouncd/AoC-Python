from aoc2019.intcode import VM
from math_extra import sign


def solve(data: str) -> None:
    arcade = VM(data)
    for part in 1, 2:
        arcade.reset()
        arcade[0] = part
        screen = {}
        paddle = ball = -1
        for x in arcade:
            if x is None:
                arcade.send(sign(ball - paddle))
                continue
            y, tile_id = arcade.get(2)
            if tile_id == 3:
                paddle = x
            elif tile_id == 4:
                ball = x
            screen[x,y] = tile_id
        if part == 1:
            print(sum(v for v in screen.values() if v == 2))
        else:
            print(screen[-1, 0])


if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
