import itertools as it
import re
import sys
from collections import Counter


def parse(inp: str) -> list[tuple[int, int, int, int]]:
    regex = re.compile(",|(?: -> )")
    return [tuple(map(int, regex.split(line))) for line in inp.splitlines()]


def part1(inp: list[tuple[int, int, int, int]]) -> int:
    lines = filter(lambda x: x[0] == x[2] or x[1] == x[3], inp)
    l = []
    for line in lines:
        x1, y1, x2, y2 = line
        for p in it.product(
            range(min(x1, x2), max(x1, x2) + 1),
            range(min(y1, y2), max(y1, y2) + 1),
        ):
            l.append(p)
    return len([c for _, c in Counter(l).items() if c >= 2])


def part2(inp: list[tuple[int, int, int, int]]) -> int:
    l = []
    for line in inp:
        x1, y1, x2, y2 = line
        xstep = 1 if x1 < x2 else -1
        ystep = 1 if y1 < y2 else -1
        for p in it.zip_longest(
            range(x1, x2 + xstep, xstep),
            range(y1, y2 + ystep, ystep),
            fillvalue=x1 if x1 == x2 else y1,
        ):
            l.append(p)
    return len([c for _, c in Counter(l).items() if c >= 2])


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
