__all__ = [
    "integers",
    "parser",
]

import re
from itertools import chain, repeat
from typing import Callable, Iterable, Optional


def integers(string: str) -> list[int]:
    return [int(x) for x in re.findall(r"(?:(?<!\d)-)?\d+", string)]

def parser(pattern: str, string: str, formatters: Optional[Iterable[Optional[Callable]]] = None) -> tuple:
    vals = []
    if (m := re.search(pattern, string)) is None:
        raise ValueError("empty match")
    for g, func in zip(m.groups(), chain(formatters or [], repeat(None))):
        vals.append(g if func is None else func(g))
    return tuple(vals)