import re
import sys
from collections import Counter


def add_tuples(a, b):
    return tuple((i + j for i, j in zip(a, b)))


def parse(lines: list[str]) -> list[list[tuple[int, int, int]]]:
    p = re.compile(
        r"p=<(-?\d+,-?\d+,-?\d+)>, v=<(-?\d+,-?\d+,-?\d+)>, a=<(-?\d+,-?\d+,-?\d+)>"
    )
    return [
        [tuple(int(n) for n in g.split(",")) for g in p.match(line).groups()]
        for line in lines
    ]


def part1(particles: list[list[tuple[int, int, int]]]) -> int:
    t = 1000000
    particles = [
        tuple((p + v * t + a / 2 * t * t for p, v, a in zip(p, v, a)))
        for p, v, a in particles
    ]
    return min(((sum(map(abs, p)), i) for i, p in enumerate(particles)))[1]


def part2(particles: list[list[tuple[int, int, int]]]) -> int:
    for i in range(10000):
        print(i, end="\r")
        pos = Counter()
        for p in particles:
            p[1] = add_tuples(p[1], p[2])
            p[0] = add_tuples(p[0], p[1])
            pos[p[0]] += 1
        particles = [p for p in particles if pos[p[0]] == 1]
    return len(particles)


if __name__ == "__main__":
    inp = parse(sys.stdin.read().splitlines())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
