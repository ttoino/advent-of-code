import sys


def solve(instructions: list[list[str]], part2: bool) -> int:
    registers = {c: 0 for c in "abcd"}
    registers["c"] = int(part2)
    ip = 0

    while 0 <= ip < len(instructions):
        match instructions[ip]:
            case ["cpy", x, y]:
                registers[y] = registers[x] if x in "abcd" else int(x)
            case ["inc", x]:
                registers[x] += 1
            case ["dec", x]:
                registers[x] -= 1
            case ["jnz", x, y]:
                if (registers[x] if x in "abcd" else int(x)) != 0:
                    ip += int(y)
                    continue

        ip += 1

    return registers["a"]


if __name__ == "__main__":
    instructions = [i.split() for i in sys.stdin.readlines()]

    print(f"Part 1: {solve(instructions, False)}")
    print(f"Part 2: {solve(instructions, True)}")
