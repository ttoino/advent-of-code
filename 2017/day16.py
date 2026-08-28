import sys
from string import ascii_lowercase


def part1(inp: list[str]) -> str:
    programs = list(ascii_lowercase[:16])
    for instruction in inp:
        match (instruction[0], instruction[1:].split('/')):
            case ['s', [x]]:
                x = int(x)
                programs = programs[-x:] + programs[:-x]
            case ['x', [a, b]]:
                a, b = (int(a), int(b))
                programs[a], programs[b] = (programs[b], programs[a])
            case ['p', [a, b]]:
                a, b = (programs.index(a), programs.index(b))
                programs[a], programs[b] = (programs[b], programs[a])
    return ''.join(programs)


def part2(inp: list[str]) -> str:
    programs = list(ascii_lowercase[:16])
    instructions = inp
    s = []
    for i in range(1000000000):
        if programs in s:
            return ''.join(s[1000000000 % i])
        s.append(programs[:])
        for instruction in instructions:
            match (instruction[0], instruction[1:].split('/')):
                case ['s', [x]]:
                    x = int(x)
                    programs = programs[-x:] + programs[:-x]
                case ['x', [a, b]]:
                    a, b = (int(a), int(b))
                    programs[a], programs[b] = (programs[b], programs[a])
                case ['p', [a, b]]:
                    a, b = (programs.index(a), programs.index(b))
                    programs[a], programs[b] = (programs[b], programs[a])
    return ''.join(programs)


if __name__ == "__main__":
    inp = input().strip().split(',')

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
