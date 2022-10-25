from aocd import data

from intcode import *

BLOCK = 2
PADDLE = 3
BALL = 4

LEFT = -1
NEUTRAL = 0
RIGHT = 1


def play(freeplay=False):
    arcade = Intcode(data)
    if freeplay:
        arcade[0] = 2
    screen = {}
    while True:
        try:
            packet = arcade.read(3)
            if len(packet) != 3:
                break
            x, y, tile_id = packet
            screen[x, y] = tile_id
        except NoInput:
            paddle_x = next(x for (x, _), val in screen.items()
                            if val == PADDLE)
            ball_x = next(x for (x, _), val in screen.items() if val == BALL)
            if ball_x < paddle_x:
                arcade.write(LEFT)
            elif paddle_x < ball_x:
                arcade.write(RIGHT)
            else:
                arcade.write(NEUTRAL)
    return screen


print(sum(1 for v in play().values() if v == BLOCK))
print(play(True)[-1, 0])
