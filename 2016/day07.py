import sys
import more_itertools as mit
import re


def part1(inp: list[list[str]]) -> int:
    s = 0

    for ip in inp:
        supports = [False, True]
        for i, part in enumerate(ip):
            for a, b, c, d in mit.windowed(part, 4):
                if a == d and b == c and a != b:
                    supports[i % 2] = not (i % 2)

        s += supports[0] and supports[1]

    return s


def part2(inp: list[list[str]]) -> int:
    s = 0

    for ip in inp:
        ss, hs = mit.partition(lambda x: x[0] % 2, enumerate(ip))
        abas = [
            (a, b, c)
            for _, s in ss
            for a, b, c in mit.triplewise(s)
            if a == c and b != a
        ]

        s += any("".join((b, a, b)) in s for _, s in hs for a, b, a in abas)

    return s


if __name__ == "__main__":
    p = re.compile(r"\[|\]")
    inp = [p.split(i) for i in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
