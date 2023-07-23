from itertools import islice
from typing import Iterable, Iterator, Sequence, TypeVar


V = TypeVar("V")


def windows(seq: Sequence[V], size: int) -> Iterator[Sequence[V]]:
    """Given sequence `seq`, yields subsequences of length `size` representing a rolling window across `seq`."""
    for i in range(0, len(seq) - size + 1):
        yield seq[i : i + size]


def chunks(iterable: Iterable[V], size: int) -> Iterator[tuple[V, ...]]:
    """Yields tuples of length `size` such that, when concatenated, comprise the original elements of `iterable`.

    Note: if `size` does not divide evenly into the number of elements in `iterable`, the last tuple will have fewer elements."""
    it = iter(iterable)
    while True:
        t = tuple(islice(it, size))
        if not t:
            break
        yield t


def main():
    xs = list(range(10))
    for c in chunks(xs, 3):
        print(c)


if __name__ == "__main__":
    main()
