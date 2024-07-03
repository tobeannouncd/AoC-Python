import json


def solve(data: str) -> None:
    obj = json.loads(data)

    for part in 1,2:
        todo, total = [obj], 0
        while todo:
            cur = todo.pop()
            if isinstance(cur, dict):
                if part == 1 or 'red' not in cur.values():
                    todo.extend(cur.values())
            elif isinstance(cur, list):
                todo.extend(cur)
            elif isinstance(cur, (int, float)):
                total += cur
        print(total)


if __name__ == '__main__':
    from aocd import data
    assert isinstance(data, str)
    solve(data)
