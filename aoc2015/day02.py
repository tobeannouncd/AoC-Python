from parsing import integers


def area(package):
    length, width, height = sorted(package)
    return 2 * (length * width + length * height + width * height) + length * width


def ribbon(package):
    length, width, height = sorted(package)
    return 2 * (length + width) + length * width * height


def solve(data: str) -> None:
    packages = [integers(line) for line in data.splitlines()]
    print(sum(area(package) for package in packages))
    print(sum(ribbon(package) for package in packages))


def main():
    from aocd import data

    assert isinstance(data, str)
    solve(data)


if __name__ == "__main__":
    main()
