__all__ = [
    "sign",
]

def sign(x: int | float) -> int:
    return int(x // abs(x)) if x else 0