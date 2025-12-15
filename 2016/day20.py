import sys
from typing import cast
from intervaltree import IntervalTree


def solve(inp: list[tuple[int, int]]) -> tuple[int, int]:
    tree = IntervalTree()
    tree[0:4294967296] = 1

    for s, e in inp:
        tree.chop(s, e + 1)

    return tree.begin(), sum(i.end - i.begin for i in tree)


if __name__ == "__main__":
    inp = [
        cast("tuple[int, int]", tuple(map(int, i.split("-"))))
        for i in sys.stdin.readlines()
    ]

    part1, part2 = solve(inp)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
