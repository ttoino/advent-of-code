import sys
from collections import defaultdict


def parse(l: list[int]) -> tuple[list[int], int]:
    children, entries, *l = l
    result = 0
    for i in range(children):
        l, s = parse(l)
        result += s
    return (l[entries:], result + sum(l[:entries]))


def parse_p2(l: list[int]) -> tuple[list[int], int]:
    children_count, entries, *l = l
    children = defaultdict(lambda: 0)
    for i in range(children_count):
        l, s = parse_p2(l)
        children[i + 1] = s
    return (
        l[entries:],
        sum(l[:entries])
        if children_count == 0
        else sum((children[i] for i in l[:entries])),
    )


def part1(inp: list[int]):
    return parse(inp)[1]


def part2(inp: list[int]):
    return parse_p2(inp)[1]


if __name__ == "__main__":
    inp = [int(n) for n in sys.stdin.read().strip().split()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
