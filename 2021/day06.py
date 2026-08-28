import sys
from collections import Counter


def part1(inp: list[int]) -> int:
    fishes = list(inp)
    for i in range(80):
        print(i, end="\r")
        new_fishes = Counter(fishes)[0]
        fishes = [6 if f == 0 else f - 1 for f in fishes] + [8] * new_fishes
    return len(fishes)


def part2(inp: list[int]) -> int:
    fishes = list(inp)
    zeros = Counter(fishes)
    new_zeros = Counter()
    for i in range(256):
        new_zeros[(i + 2) % 7] = zeros[i % 7]
        zeros[i % 7] += new_zeros[i % 7]
        new_zeros[i % 7] = 0
    return sum(zeros.values()) + sum(new_zeros.values())


if __name__ == "__main__":
    inp = list(map(int, sys.stdin.readline().split(",")))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
