import functools as ft
import sys
from collections import Counter


def part1(inp: list[str]) -> int:
    gamma, epsilon = map(
        lambda x: int(x, 2),
        ft.reduce(
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            map(
                lambda c: (c.most_common(1)[0][0], c.most_common(2)[-1][0]),
                map(Counter, zip(*inp)),
            ),
        ),
    )
    return gamma * epsilon


def part2(inp: list[str]) -> int:
    ll = list(inp)
    l = list(ll)
    i = 0
    while len(l) > 1:
        c = Counter((n[i] for n in l)).most_common(2)
        mcb = "1" if c[0][1] == c[-1][1] else c[0][0]
        l = list(filter(lambda x: x[i] == mcb, l))
        i += 1
    ogr = int(l[0], 2)
    l = list(ll)
    i = 0
    while len(l) > 1:
        c = Counter((n[i] for n in l)).most_common(2)
        lcb = "0" if c[0][1] == c[-1][1] else c[-1][0]
        l = list(filter(lambda x: x[i] == lcb, l))
        i += 1
    co2sr = int(l[0], 2)
    return ogr * co2sr


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
