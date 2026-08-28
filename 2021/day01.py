import itertools as it
import sys


def part1(inp: list[int]) -> int:
    return sum(curr > prev for prev, curr in it.pairwise(inp))


def part2(inp: list[int]) -> int:
    return sum(
        curr > prev
        for prev, curr in it.pairwise(
            map(
                sum,
                (
                    (a, b, c)
                    for (a, _), (b, c) in it.pairwise(it.pairwise(inp))
                ),
            )
        )
    )


if __name__ == "__main__":
    inp = list(map(int, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
