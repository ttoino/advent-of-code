import re
import sys



def parse(s: str) -> list[tuple[int, int, int, int]]:
    return [tuple(map(int, re.split('[,-]', line))) for line in s.splitlines()]


def part1(inp: list[tuple[int, int, int, int]]):
    return sum((int(a[0] >= a[2] and a[1] <= a[3] or (a[0] <= a[2] and a[1] >= a[3])) for a in inp))


def part2(inp: list[tuple[int, int, int, int]]):
    return sum((int(len(set(range(a[0], a[1] + 1)).intersection(set(range(a[2], a[3] + 1)))) > 0) for a in inp))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
