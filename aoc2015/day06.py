from collections import defaultdict
from utils import *


def solve(data: str) -> None:
    lights = {}
    for line in data.splitlines():
        match line.split():
            case ["turn", "on", a, _, b]:
                xmin, ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        lights[x,y] = 1
            case ['turn','off',a,_,b]:
                xmin,ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        lights[x,y] = 0
            case ['toggle',a,_,b]:
                xmin, ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        val = lights.get((x,y),0)
                        lights[x, y] = (val + 1) % 2
    print(sum(lights.values()))

    lights = defaultdict(int)
    for line in data.splitlines():
        match line.split():
            case ["turn", "on", a, _, b]:
                xmin, ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        lights[x,y] += 1
            case ['turn','off',a,_,b]:
                xmin,ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        lights[x,y] = max(lights[x,y]-1, 0)
            case ['toggle',a,_,b]:
                xmin, ymin = map(int, a.split(','))
                xmax, ymax = map(int, b.split(','))
                for x in range(xmin,xmax+1):
                    for y in range(ymin,ymax+1):
                        lights[x, y] +=  2
    print(sum(lights.values()))



def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
