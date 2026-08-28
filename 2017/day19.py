import sys


def add_tuples(a, b):
    return tuple((i + j for i, j in zip(a, b)))


def part1(inp: list[str]) -> str:
    fl = inp[0]
    w = len(fl)
    pos = (fl.index("|"), 0)
    dir = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    map = "".join(inp[1:])
    h = len(map) // w
    result = ""

    def get(p):
        return map[p[0] + p[1] * w]

    while 0 <= pos[0] < w and 0 <= pos[1] < h:
        c = get(pos)
        if c.isalpha():
            result += c
        if c == "+":
            dir -= 1 if get(add_tuples(pos, dirs[dir - 1])) != " " else 3
            dir %= 4
        if c == " ":
            break
        pos = add_tuples(pos, dirs[dir])
    return result


def part2(inp: list[str]) -> int:
    fl = inp[0]
    w = len(fl)
    pos = (fl.index("|"), 0)
    dir = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    map = "".join(inp[1:])
    h = len(map) // w
    result = ""
    steps = 1

    def get(p):
        return map[p[0] + p[1] * w]

    while 0 <= pos[0] < w and 0 <= pos[1] < h:
        c = get(pos)
        if c.isalpha():
            result += c
        if c == "+":
            dir -= 1 if get(add_tuples(pos, dirs[dir - 1])) != " " else 3
            dir %= 4
        if c == " ":
            break
        pos = add_tuples(pos, dirs[dir])
        steps += 1
    return steps


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
