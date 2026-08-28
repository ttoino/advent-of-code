import re
import sys

import functools as ft
import operator as op
from collections import defaultdict


pattern = re.compile(r'\d+')


def part1(inp: list[str]) -> int:
    lines = inp
    result = 0
    for y, line in enumerate(lines):
        line = line.strip()
        for match in pattern.finditer(line):
            num = int(match.group())
            part = False
            for x in range(max(0, match.start() - 1), min(match.end() + 1, len(line))):
                for yy in range(max(0, y - 1), min(y + 2, len(lines))):
                    part = part or (not lines[yy][x].isdigit() and lines[yy][x] != '.')
            if part:
                result += num
    return result


def part2(inp: list[str]) -> int:
    lines = inp
    gears = defaultdict(set)
    for y, line in enumerate(lines):
        line = line.strip()
        for match in pattern.finditer(line):
            num = int(match.group())
            for x in range(max(0, match.start() - 1), min(match.end() + 1, len(line))):
                for yy in range(max(0, y - 1), min(y + 2, len(lines))):
                    if lines[yy][x] == '*':
                        gears[x, yy].add(num)
    result = sum((ft.reduce(op.mul, gear) for gear in gears.values() if len(gear) == 2))
    return result


if __name__ == "__main__":
    inp = [line.strip() for line in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
