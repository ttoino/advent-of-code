import itertools as it
import sys


def part1(inp: list[list[int]]) -> int:
    return sum((max(i) - min(i) for i in inp))


def part2(inp: list[list[int]]) -> int:
    return sum((max(c) // min(c) for c in (c for i in inp for c in it.combinations(i, 2) if max(c) % min(c) == 0)))


if __name__ == "__main__":
    inp = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
