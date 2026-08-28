import sys
from collections import defaultdict


def add_tuples(a, b):
    return tuple((i + j for i, j in zip(a, b)))


def part1(inp: list[str]) -> int:
    infected = {
        (x, y)
        for y, l in enumerate(inp, start=-12)
        for x, c in enumerate(l.strip(), start=-12)
        if c == "#"
    }
    pos = (0, 0)
    dir = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    result = 0
    for i in range(10000):
        dir += 1 + 2 * (pos not in infected)
        dir %= 4
        if pos in infected:
            infected.remove(pos)
        else:
            infected.add(pos)
            result += 1
        pos = add_tuples(pos, dirs[dir])
    return result


def part2(inp: list[str]) -> int:
    nodes = defaultdict(
        lambda: 3,
        (
            ((x, y), 1)
            for y, l in enumerate(inp, start=-12)
            for x, c in enumerate(l.strip(), start=-12)
            if c == "#"
        ),
    )
    pos = (0, 0)
    dir = 0
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    result = 0
    for i in range(10000000):
        print(f"{i / 100000:2.0f}%", end="\r")
        dir += nodes[pos]
        dir %= 4
        nodes[pos] += 1
        nodes[pos] %= 4
        result += nodes[pos] == 1
        pos = add_tuples(pos, dirs[dir])
    return result


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
