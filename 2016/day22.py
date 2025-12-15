import itertools as it
import sys
from typing import cast
import re


def part1(nodes: list[tuple[int, int, int, int, int, int]]) -> int:
    pairs = [(a, b) for a, b in it.permutations(nodes, 2) if a[3] != 0 and a[3] <= b[4]]
    return len(pairs)


def part2(nodes: list[tuple[int, int, int, int, int, int]]) -> int:
    nodes = sorted(nodes, key=lambda x: (x[1], x[0]))
    print(
        "\n".join(
            " ".join(
                "!"
                if x == 0 and y == 0
                else (
                    "G"
                    if x == 32 and y == 0
                    else ("#" if size > 400 else ("_" if used == 0 else "."))
                )
                for x, y, size, used, avail, percent in line
            )
            for y, line in it.groupby(nodes, key=lambda x: x[1])
        )
    )

    return -1


if __name__ == "__main__":
    p = re.compile(r"-[xy]|[T%]?\s+")
    inp = [
        cast("tuple[int, int, int, int, int, int]", tuple(map(int, p.split(i)[1:])))
        for i in sys.stdin.readlines()[2:]
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
