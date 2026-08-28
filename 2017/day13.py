import itertools as it
import sys


def part1(inp: list[tuple[int, int]]) -> int:
    layers = inp
    return sum((d * r for d, r in layers if d % (r * 2 - 2) == 0))


def part2(inp: list[tuple[int, int]]) -> int:
    layers = inp
    for i in it.count():
        if sum(((d + i) % (r * 2 - 2) == 0 for d, r in layers)) == 0:
            return i
            break


if __name__ == "__main__":
    inp = [
        tuple(map(int, line.split(": ")))
        for line in sys.stdin.read().splitlines()
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
