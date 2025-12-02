import sys


def part1(inp: list[str]):
    s = 0

    for i in inp:
        s += len(i.strip())
        s -= len(eval(i))

    return s


def part2(inp: list[str]):
    s = 0

    for i in inp:
        s += len(i.strip().replace("\\", "\\\\").replace('"', '\\"')) + 2
        s -= len(i.strip())

    return s


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
