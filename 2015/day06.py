import sys


def parse(i: str) -> tuple[str, int, int, int, int]:
    action, start, _, end = i.removeprefix("turn ").split()
    sx, sy = map(int, start.split(","))
    ex, ey = map(int, end.split(","))

    return action, sx, sy, ex, ey


def part1(inp: list[tuple[str, int, int, int, int]]):
    a = [False for i in range(1000 * 1000)]

    for action, sx, sy, ex, ey in inp:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                match action:
                    case "on":
                        a[x + y * 1000] = True
                    case "off":
                        a[x + y * 1000] = False
                    case "toggle":
                        a[x + y * 1000] = not a[x + y * 1000]

    return sum(a)


def part2(inp: list[tuple[str, int, int, int, int]]):
    a = [0 for i in range(1000 * 1000)]

    for action, sx, sy, ex, ey in inp:
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                match action:
                    case "on":
                        a[x + y * 1000] += 1
                    case "off":
                        a[x + y * 1000] = max(a[x + y * 1000] - 1, 0)
                    case "toggle":
                        a[x + y * 1000] += 2

    return sum(a)


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
