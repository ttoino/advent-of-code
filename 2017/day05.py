import itertools as it
import sys


def part1(inp: list[int]) -> int:
    jumps = inp[:]
    ip = 0
    for i in it.count():
        if ip >= len(jumps) or ip < 0:
            return i
            break
        temp = ip
        ip += jumps[temp]
        jumps[temp] += 1


def part2(inp: list[int]) -> int:
    jumps = inp[:]
    ip = 0
    for i in it.count():
        if ip >= len(jumps) or ip < 0:
            return i
            break
        temp = ip
        ip += jumps[temp]
        jumps[temp] += (jumps[temp] < 3) - (jumps[temp] >= 3)


if __name__ == "__main__":
    inp = [int(line) for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
