from functools import cache


def solve(data) -> None:
    connections: dict[str, str] = {}
    for line in data.splitlines():
        inp, wire = line.split(' -> ')
        connections[wire] = inp

    @cache
    def get_val(wire: str) -> int:
        if wire.isnumeric():
            return int(wire)
        inp = connections[wire]
        if inp.isnumeric():
            return int(inp)
        match inp.split():
            case [x, 'AND', y]:
                return get_val(x) & get_val(y)
            case [x, 'OR', y]:
                return get_val(x) | get_val(y)
            case [x, 'LSHIFT', y]:
                return get_val(x) << get_val(y)
            case [x, 'RSHIFT', y]:
                return get_val(x) >> get_val(y)
            case ['NOT', x]:
                return get_val(x) ^ 0xFFFF
            case [x]:
                return get_val(x)
        return -1
    
    a_val = get_val('a')
    print(a_val)
    connections['b'] = str(a_val)
    get_val.cache_clear()
    print(get_val('a'))


def main():
    from aocd import data
    solve(data)


if __name__ == '__main__':
    main()
