from contextlib import contextmanager
from time import perf_counter

__all__ = ['benchmark']


class Timer:
    def __init__(self) -> None:
        self._splits = [perf_counter()]

    def split(self, label="split") -> None:
        self._splits.append(perf_counter())
        diff = self._splits[-1] - self._splits[-2]
        print(f"{diff:.3f}s ({label})")

    def end(self) -> None:
        t = perf_counter() - self._splits[0]
        print(f"{t:.3f}s (total)")


@contextmanager
def benchmark():
    t = Timer()
    yield t
    t.end()