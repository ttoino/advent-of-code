import sys
import re


def solve(instructions: list[list[str]], part: int):
    registers = {"a": part - 1, "b": 0}
    ip = 0

    while 0 <= ip < len(instructions):
        match instructions[ip]:
            case ["hlf", r]:
                registers[r] //= 2
            case ["tpl", r]:
                registers[r] *= 3
            case ["inc", r]:
                registers[r] += 1
            case ["jmp", offset]:
                ip += int(offset)
                continue
            case ["jie", r, offset]:
                if registers[r] % 2 == 0:
                    ip += int(offset)
                    continue
            case ["jio", r, offset]:
                if registers[r] == 1:
                    ip += int(offset)
                    continue
        ip += 1

    return registers["b"]


if __name__ == "__main__":
    instructions = [re.split(r",? ", i.strip()) for i in sys.stdin.readlines()]

    print(f"Part 1: {solve(instructions, 1)}")
    print(f"Part 1: {solve(instructions, 2)}")
