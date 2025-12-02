import sys


def part1(inp: list[tuple[int, int, int]]):
    s = 0
    for l, w, h in inp:
        s += 3 * l * w + 2 * w * h + 2 * h * l
    return s


def part2(inp: list[tuple[int, int, int]]):
    s = 0
    for l, w, h in inp:
        s += l + l + w + w + l * w * h
    return s


if __name__ == "__main__":
    inp: list[tuple[int, int, int]] = [
        tuple(sorted(map(int, i.split("x")))) for i in sys.stdin.readlines()
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
