import sys


def t(x):
    return x * (x + 1) // 2


def part1(inp: list[int]) -> int:
    crabs = list(inp)
    pos = sorted(crabs)[len(crabs) // 2]
    return sum(abs(pos - x) for x in crabs)


def part2(inp: list[int]) -> int:
    crabs = list(inp)
    return min(sum(t(abs(i - x)) for x in crabs) for i in range(max(crabs)))


if __name__ == "__main__":
    inp = list(map(int, sys.stdin.readline().split(",")))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
