from collections import defaultdict
from dataclasses import dataclass, field
from functools import cached_property, partial
from io import StringIO
from typing import Self

@dataclass
class Folder:
    files: int = 0
    children: dict[str, Self] = field(default_factory=dict)

    @cached_property
    def size(self) -> int:
        return self.files + sum(child.size for child in self.children.values())


def solve(data: str) -> None:
    inp = StringIO(data)

    
    root = current = Folder(children = {"/": Folder()})
    dirs = [root]
    stack = []
    for x in iter(inp.readline, ""):
        match x.split():
            case ['$', "cd", ".."]:
                current = stack.pop()
            case ['$', "cd", name]:
                stack.append(current)
                current = current.children[name]
            case ["$", "ls"]:
                pass
            case ["dir", d]:
                current.children[d] = Folder()
                dirs.append(current.children[d])
            case [size, _]:
                current.files += int(size)

    print(sum(d.size for d in dirs if d.size <= 100000))

    needed = root.size - 40000000
    print(min(d.size for d in dirs if d.size >= needed))

if __name__ == "__main__":
    from aocd import data

    assert isinstance(data, str)
    solve(data)
