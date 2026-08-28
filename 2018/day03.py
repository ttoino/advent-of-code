import sys

import itertools as it
import re
from collections import Counter


def parse(i: str) -> tuple[int, int, int, int, int]:
    pattern = re.compile('#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)')
    m = pattern.match(i)
    return int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5])


def part1(inp: list[tuple[int, int, int, int, int]]):
    c = Counter()
    for _, x, y, w, h in inp:
        for p in it.product(range(x, x + w), range(y, y + h)):
            c[p] += 1
    return len([count for _, count in c.items() if count >= 2])


def part2(inp: list[tuple[int, int, int, int, int]]):
    d = {}
    claims = set()
    for id, x, y, w, h in inp:
        claim = set(it.product(range(x, x + w), range(y, y + h)))
        claims.add(id)
        for other_id, s in d.items():
            if len(s & claim) > 0:
                claims.discard(other_id)
                claims.discard(id)
        d[id] = claim
    return next(iter(claims))


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
