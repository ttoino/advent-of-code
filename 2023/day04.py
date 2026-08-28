import sys
from collections import defaultdict


def parse(i: str) -> tuple[set[int], set[int]]:
    line = i.split(":")[1].strip()
    mine, winning = line.split("|")
    return set(map(int, mine.split())), set(map(int, winning.split()))


def part1(inp: list[tuple[set[int], set[int]]]) -> int:
    result = 0
    for mine, winning in inp:
        count = len(mine & winning)
        if count != 0:
            result += 2 ** (count - 1)
    return result


def part2(inp: list[tuple[set[int], set[int]]]) -> int:
    counter = defaultdict(lambda: 1)
    for i, (mine, winning) in enumerate(inp):
        counter[i]
        count = len(mine & winning)
        for j in range(1, count + 1):
            counter[i + j] += counter[i]
    return sum(counter.values())


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
