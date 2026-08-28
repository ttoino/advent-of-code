import sys

import itertools as it


def part1(inp: list[int]):
    return sum(inp)


def part2(inp: list[int]):
    f = 0
    s = {0}
    for i in it.cycle(inp):
        f += i
        if f in s:
            return f
        s.add(f)


if __name__ == "__main__":
    inp = [int(i.strip()) for i in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
