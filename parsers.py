__all__ = [
    "parse_ints",
]

import re
from typing import Any, Callable, Iterator, Mapping


def parse_ints(s: str) -> Iterator[int]:
    return map(int, re.findall(r"(?:(?<!\d)-)?\d+", s))


def parse_pattern(pattern: str, string: str, transforms: Mapping[int,Callable[[str],Any]] | None = None) -> list[Any]:
    if (m:=re.search(pattern, string)) is None:
        raise ValueError("Pattern not found")
    vals = list(m.groups())
    for i, func in (transforms or {}).items():
        vals[i] = func(vals[i])
    return vals


def main():
    pass


if __name__ == "__main__":
    main()
