import sys
from collections import defaultdict


def part1(inp: list[list[str]]) -> int:
    registers = defaultdict(lambda: 0)
    result = 0
    ip = 0

    def get(r: str):
        return registers[r] if r.isalpha() else int(r)

    instructions = inp
    while len(instructions) > ip >= 0:
        match instructions[ip]:
            case ["set", x, y]:
                registers[x] = get(y)
            case ["sub", x, y]:
                registers[x] -= get(y)
            case ["mul", x, y]:
                registers[x] *= get(y)
                result += 1
            case ["jnz", x, y]:
                if get(x) != 0:
                    ip += get(y)
                    continue
        ip += 1
    return result


def part2(inp: list[list[str]]) -> int:
    h = 0
    for b in range(93 * 100 + 100000, 93 * 100 + 100000 + 17000 + 1, 17):
        for d in range(2, b):
            if b % d == 0:
                h += 1
                break
    return h


if __name__ == "__main__":
    inp = [line.split() for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
