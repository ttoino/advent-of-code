import sys
from string import ascii_lowercase


def react(s: str):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1].swapcase():
            s = s[:i] + s[i + 2 :]
            i -= 1
            continue
        i += 1
    return len(s)


def part1(inp: str):
    return react(inp)


def part2(inp: str):
    return min(
        (
            react("".join((c for c in inp if c.lower() != l)))
            for l in ascii_lowercase
        )
    )


if __name__ == "__main__":
    inp = sys.stdin.read().strip()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
