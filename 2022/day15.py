import re
import sys

SIZE = 4000000
PATTERN = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)


def dist(x, y, bx, by):
    return abs(x - bx) + abs(y - by)


def parse(s: str) -> list[tuple[int, int, int, int]]:
    return [
        tuple(map(int, PATTERN.match(line).groups()))
        for line in s.splitlines()
    ]


def part1(inp: list[tuple[int, int, int, int]]):
    sensors = inp
    impossible = set()
    beacons = set()
    for x, y, bx, by in sensors:
        d = abs(x - bx) + abs(y - by)
        ydist = abs(2000000 - y)
        xdist = d - ydist
        impossible.update(range(x - xdist, x + xdist + 1))
        if by == 2000000:
            beacons.add(bx)
    return len(impossible - beacons)


def part2(inp: list[tuple[int, int, int, int]]):
    sensors = [(x, y, dist(x, y, bx, by)) for x, y, bx, by in inp]
    points = []
    for x, y, d in sensors:
        for px in range(x - d - 1, x + d + 2):
            if not 0 <= px <= SIZE:
                continue
            dd = abs(x - px)
            py1 = y + d + 1 - dd
            py2 = y - (d + 1 - dd)
            if 0 <= py1 <= SIZE:
                points.append((px, py1))
            if 0 <= py2 <= SIZE:
                points.append((px, py2))
        for x, y, d in sensors:
            points = list(filter(lambda p: dist(x, y, p[0], p[1]) > d, points))
        if len(points) > 0:
            break
    x, y = points[0]
    return x * 4000000 + y


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
