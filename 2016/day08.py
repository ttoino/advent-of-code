import sys
from time import sleep
import more_itertools as mit
import re


def print_code(code):
    print(
        "\x1b[H\x1b[J"
        + "\n".join(
            "".join("#" if c else " " for c in line) for line in mit.chunked(code, 50)
        )
    )
    sleep(0.1)


def get(code: list[int], x: int, y: int) -> int:
    return code[(x % 50) + (y % 6) * 50]


def set(code: list[int], x: int, y: int, v):
    code[(x % 50) + (y % 6) * 50] = v


def solve(inp: list[list[str]]) -> tuple[int, str]:
    code = [0 for _ in range(50 * 6)]

    for i in inp:
        new_code = [i for i in code]

        match i:
            case ["rect", size]:
                w, h = map(int, size.split("x"))
                for x in range(w):
                    for y in range(h):
                        set(new_code, x, y, 1)
            case ["rotate", "row", "y", y, "by", b]:
                y = int(y)
                b = int(b)
                for x in range(50):
                    set(new_code, x, y, get(code, x - b, y))
            case ["rotate", "column", "x", x, "by", b]:
                x = int(x)
                b = int(b)
                for y in range(6):
                    set(new_code, x, y, get(code, x, y - b))

        code = new_code
        print_code(code)

    return sum(code), "Look above"


if __name__ == "__main__":
    p = re.compile(r" |=")
    inp = [p.split(i) for i in sys.stdin.readlines()]

    part1, part2 = solve(inp)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
