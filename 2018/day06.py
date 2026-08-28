import itertools as it
import sys


def part1(inp: list[tuple[int, int]]):
    points = inp
    areas = [0 for _ in points]
    infinite = [False for _ in points]
    min_x = min(points)[0]
    max_x = max(points)[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_y = max(points, key=lambda x: x[1])[1]
    for x, y in it.product(range(min_x, max_x + 1), range(min_y, max_y + 1)):
        min_dist = 10000000000000
        valid = True
        index = -1
        for i, (px, py) in enumerate(points):
            dist = abs(x - px) + abs(y - py)
            if dist == min_dist:
                valid = False
            elif dist < min_dist:
                valid = True
                min_dist = dist
                index = i
        if not valid:
            continue
        areas[index] += 1
        if x == min_x or x == max_x or y == min_y or (y == max_y):
            infinite[index] = True
    return max((a for i, a in enumerate(areas) if not infinite[i]))


def part2(inp: list[tuple[int, int]]):
    points = inp
    return len(
        [
            (x, y)
            for x, y in it.product(
                range(min(points)[0], max(points)[0] + 1),
                range(
                    min(points, key=lambda x: x[1])[1],
                    max(points, key=lambda x: x[1])[1] + 1,
                ),
            )
            if sum((abs(x - px) + abs(y - py) for px, py in points)) < 10000
        ]
    )


if __name__ == "__main__":
    inp = [
        tuple(map(int, i.strip().split(","))) for i in sys.stdin.readlines()
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
