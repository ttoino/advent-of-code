import re
import sys
from collections import defaultdict


def part1(inp: list[str]) -> int:
    registers = defaultdict(lambda: 0)
    p = re.compile(r'(\w+) (inc|dec) (-?\d+) if ((\w+) [!<>=]=? -?\d+)')
    for i in inp:
        m = p.match(i)
        if eval(m[4].replace(m[5], f"registers['{m[5]}']")):
            registers[m[1]] += int(m[3]) * ((m[2] == 'inc') - (m[2] == 'dec'))
    return max(registers.values())


def part2(inp: list[str]) -> int:
    registers = defaultdict(lambda: 0)
    values = set()
    p = re.compile(r'(\w+) (inc|dec) (-?\d+) if ((\w+) [!<>=]=? -?\d+)')
    for i in inp:
        m = p.match(i)
        if eval(m[4].replace(m[5], f"registers['{m[5]}']")):
            registers[m[1]] += int(m[3]) * ((m[2] == 'inc') - (m[2] == 'dec'))
        values |= set(registers.values())
    return max(values)


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
