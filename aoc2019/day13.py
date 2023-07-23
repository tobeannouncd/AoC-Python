from aoc2019.intcode import VM


def solve(data: str) -> None:
    for part in 1, 2:
        screen = {}
        game = VM(data)
        if part == 2:
            game.memory[0] = 2
        for x in game:
            if x is None:
                paddle = next(x for (x,_), tile in screen.items() if tile == 3)
                ball = next(x for (x,_), tile in screen.items() if tile == 4)
                diff = ball - paddle
                if diff:
                    diff //= abs(diff)
                game.send(diff)
                continue
            y = next(game)
            tile = next(game)
            screen[x,y] = tile
        if part == 1:
            print(sum(1 for tile in screen.values() if tile == 2))
        else:
            print(screen[-1, 0])



if __name__ == "__main__":
    from aocd import data
    assert isinstance(data, str)
    solve(data)
