import sys


def solve(instructions: list[list[str]], part2: bool) -> int:
    registers = {c: 0 for c in "abcd"}
    registers["a"] = 12 if part2 else 7
    ip = 0

    while 0 <= ip < len(instructions):
        match instructions[ip : ip + 5]:
            case [
                ["inc", a],
                ["dec", c],
                ["jnz", c1, "-2"],
                ["dec", d],
                ["jnz", d1, "-5"],
            ] if c == c1 and d == d1 and part2:
                registers[a] += registers[c] * registers[d]
                ip += 5
                continue

        match instructions[ip]:
            case ["cpy", x, y]:
                if y in "abcd":
                    registers[y] = registers[x] if x in "abcd" else int(x)
            case ["inc", x]:
                registers[x] += 1
            case ["dec", x]:
                registers[x] -= 1
            case ["jnz", x, y]:
                if (registers[x] if x in "abcd" else int(x)) != 0:
                    ip += registers[y] if y in "abcd" else int(y)
                    continue
            case ["tgl", x]:
                x = registers[x] if x in "abcd" else int(x)
                if 0 <= ip + x < len(instructions):
                    i = instructions[ip + x][0]
                    instructions[ip + x][0] = (
                        "dec"
                        if i == "inc"
                        else (
                            "inc"
                            if i in ("dec", "tgl")
                            else ("cpy" if i == "jnz" else "jnz")
                        )
                    )

        ip += 1

    return registers["a"]


if __name__ == "__main__":
    instructions = [i.split() for i in sys.stdin.readlines()]

    print(f"Part 1: {solve(instructions, False)}")
    print(f"Part 2: {solve(instructions, True)}")
