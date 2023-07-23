from itertools import product
from utils import *


def solve(data: str) -> None:
    xmin, xmax, ymin, ymax = ints(data)
    vx_min = 1
    while vx_min * (vx_min + 1) // 2 < xmin:
        vx_min += 1
    vx_max = xmax
    vy_min = ymin
    vy_max = -ymin - 1
    print(vy_max * (vy_max + 1) // 2)

    ans = 0
    for vx, vy in product(range(vx_min, vx_max + 1), 
                          range(vy_min, vy_max + 1)):
        pt = Point(0, 0)
        vel = Point(vx, vy)
        while pt.x <= xmax and pt.y >= ymin:
            pt += vel
            vel = Point(max(0, vel.x - 1), vel.y - 1)
            if xmin <= pt.x <= xmax and ymin <= pt.y <= ymax:
                ans += 1
                break
    print(ans)


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
