from functools import cache


def parse(line: str)-> tuple[str, dict[str, int]]:
    outer, inner = line.split(' bags contain ')
    if inner.startswith('no'):
        return outer, {}
    x = {}
    for part in inner.split(', '):
        qty, adj, color, _ = part.split()
        x[f'{adj} {color}'] = int(qty)
    return outer, x

def solve(data: str) -> None:
    bags = {}
    for o, i in map(parse, data.splitlines()):
        bags[o] = i
    
    def contains(outer, inner) -> bool:
        if inner in bags[outer]:
            return True
        return any(contains(o, inner) for o in bags[outer])
    
    print(sum(1 for b in bags if contains(b, 'shiny gold')))

    def bags_needed(outer):
        total = 0
        for inner, qty in bags[outer].items():
            total += qty + qty*bags_needed(inner)
        return total
    
    print(bags_needed('shiny gold'))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
