import sys

import itertools as it


def parse(i: str) -> list[int]:
    return [int(x) for x in i.strip().split()]


def part1(inp: list[list[int]]) -> int:
    result = 0
    for l in inp:
        ll = [l]
        while not all((x == 0 for x in ll[-1])):
            ll.append([y - x for x, y in it.pairwise(ll[-1])])
        for l in ll[::-1]:
            result += l[-1]
    return result


def part2(inp: list[list[int]]) -> int:
    result = 0
    for l in inp:
        ll = [l]
        while not all((x == 0 for x in ll[-1])):
            ll.append([y - x for x, y in it.pairwise(ll[-1])])
        prev = ll[-1][0]
        for l in ll[::-1]:
            prev = l[0] - prev
        result += prev
    return result


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
