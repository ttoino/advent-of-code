import functools as ft
import sys

opmap = {
    "forward": lambda p, x: (p[0] + x, p[1]),
    "up": lambda p, x: (p[0], p[1] - x),
    "down": lambda p, x: (p[0], p[1] + x),
}

opmap_p2 = {
    "forward": lambda p, x: (p[0] + x, p[1] + p[2] * x, p[2]),
    "up": lambda p, x: (p[0], p[1], p[2] - x),
    "down": lambda p, x: (p[0], p[1], p[2] + x),
}


def part1(inp: list[tuple[str, int]]) -> int:
    x, y = ft.reduce(lambda p, x: opmap[x[0]](p, x[1]), inp, (0, 0))
    return x * y


def part2(inp: list[tuple[str, int]]) -> int:
    x, y, _ = ft.reduce(lambda p, x: opmap_p2[x[0]](p, x[1]), inp, (0, 0, 0))
    return x * y


if __name__ == "__main__":
    inp = [
        (cmd, int(val)) for cmd, val in (line.split() for line in sys.stdin)
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
