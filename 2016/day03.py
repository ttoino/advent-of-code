import itertools as it
import sys
from typing import cast
import functools as ft
import operator as op


def part1(inp: list[tuple[int, int, int]]) -> int:
    return sum(
        ft.reduce(op.and_, (t[0] + t[1] > t[2] for t in it.permutations(triangle)))
        for triangle in inp
    )


def part2(inp: list[tuple[int, int, int]]) -> int:
    return sum(
        ft.reduce(op.and_, (t[0] + t[1] > t[2] for t in it.permutations(triangle)))
        for triangle in it.batched(it.chain(*zip(*inp)), 3)
    )


if __name__ == "__main__":
    inp = [
        cast("tuple[int, int, int]", tuple(map(int, t.split())))
        for t in sys.stdin.readlines()
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
