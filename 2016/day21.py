import itertools as it
import sys
from typing import Iterable


def part1(inp: list[list[str]], start: Iterable[str] = "abcdefgh") -> str:
    s = list(start)

    for i in inp:
        match i:
            case ["swap", "position", x, "with", "position", y]:
                x = int(x)
                y = int(y)
                s[x], s[y] = s[y], s[x]
            case ["swap", "letter", x, "with", "letter", y]:
                x = s.index(x)
                y = s.index(y)
                s[x], s[y] = s[y], s[x]
            case ["rotate", "left", x, "steps" | "step"]:
                x = int(x)
                s = s[x:] + s[:x]
            case ["rotate", "right", x, "steps" | "step"]:
                x = int(x)
                s = s[-x:] + s[:-x]
            case ["rotate", "based", "on", "position", "of", "letter", x]:
                x = s.index(x)
                x = (1 + x + (x >= 4)) % len(s)
                s = s[-x:] + s[:-x]
            case ["reverse", "positions", x, "through", y]:
                x = int(x)
                y = int(y)
                x, y = min(x, y), max(x, y)
                s[x : y + 1] = s[x : y + 1][::-1]
            case ["move", "position", x, "to", "position", y]:
                x = int(x)
                y = int(y)
                c = s[x]
                del s[x]
                s.insert(y, c)

    return "".join(s)


def part2(inp: list[list[str]]) -> str:
    o = "abcdefgh"
    target = "fbgdceah"

    for p in it.permutations(o, len(o)):
        if part1(inp, p) == target:
            return "".join(p)

    return ""


if __name__ == "__main__":
    inp = [i.split() for i in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
