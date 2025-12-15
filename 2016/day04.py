import sys
import re
from string import ascii_lowercase


def part1(inp: list[tuple[str, int, str]]) -> int:
    s = 0

    for name, id, expected in inp:
        actual = "".join(
            sorted({c for c in name if c != "-"}, key=lambda x: (-name.count(x), x))[:5]
        )
        if actual == expected:
            s += id

    return s


def part2(inp: list[tuple[str, int, str]]) -> int:
    for name, id, _ in inp:
        name = "".join(
            " " if c == "-" else ascii_lowercase[(ascii_lowercase.index(c) + id) % 26]
            for c in name[:-1]
        )

        if "north" in name:
            return id

    return -1


if __name__ == "__main__":
    pattern = re.compile(r"((?:\w+-)+)(\d+)\[(\w{5})\]")
    inp = [
        (a, int(b), c)
        for a, b, c in (pattern.match(i).groups() for i in sys.stdin.readlines())
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
