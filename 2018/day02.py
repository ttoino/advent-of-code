import itertools as it
import sys
from collections import Counter


def part1(inp: list[str]):
    twos, threes = (0, 0)
    for i in inp:
        c = Counter(i).values()
        twos += 2 in c
        threes += 3 in c
    return twos * threes


def part2(inp: list[str]):
    for a, b in it.combinations(inp, 2):
        s = "".join((a for a, b in zip(a, b) if a == b))
        if len(s) == 25:
            return s


if __name__ == "__main__":
    inp = [i.strip() for i in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
