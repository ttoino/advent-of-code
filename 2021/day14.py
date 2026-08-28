import sys

import itertools as it
from collections import Counter


def parse(inp: str) -> tuple[str, dict[str, str]]:
    lines = inp.splitlines()
    polymer = lines[0].strip()
    rules = dict(line.strip().split(" -> ") for line in lines[2:])
    return polymer, rules


def part1(inp: tuple[str, dict[str, str]]) -> int:
    polymer, rules = inp
    for i in range(10):
        n = ""
        for first, second in it.pairwise(polymer):
            n += first
            n += rules[first + second]
        n += polymer[-1]
        polymer = n
    c = Counter(polymer).values()
    return max(c) - min(c)


def part2(inp: tuple[str, dict[str, str]]) -> int:
    polymer, rules = inp
    last = polymer[-1]
    polymer = Counter(it.pairwise(polymer))
    for i in range(40):
        temp = Counter()
        for (first, second), frequency in polymer.items():
            middle = rules[first + second]
            temp[first, middle] += frequency
            temp[middle, second] += frequency
        polymer = temp
    c = Counter(last)
    for (first, second), frequency in polymer.items():
        c[first] += frequency
    return max(c.values()) - min(c.values())


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
