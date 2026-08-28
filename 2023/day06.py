import sys
from math import ceil, floor, sqrt


def part1(inp: tuple[tuple[int, ...], tuple[int, ...]]) -> int:
    times, distances = inp
    result = 1
    for time, distance in zip(times, distances):
        delta = time * time - 4 * distance
        zeros = ((time - sqrt(delta)) / 2, (time + sqrt(delta)) / 2)
        result *= floor(zeros[1] - 0.01) - ceil(zeros[0] + 0.01) + 1
    return result


def part2(inp: tuple[int, int]) -> int:
    time, distance = inp
    delta = time * time - 4 * distance
    zeros = ((time - sqrt(delta)) / 2, (time + sqrt(delta)) / 2)
    result = floor(zeros[1] - 0.01) - ceil(zeros[0] + 0.01) + 1
    return result


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    times = tuple(map(int, lines[0].strip().split()[1:]))
    distances = tuple(map(int, lines[1].strip().split()[1:]))
    time2 = int("".join(lines[0].strip().split()[1:]))
    distance2 = int("".join(lines[1].strip().split()[1:]))

    print(f"Part 1: {part1((times, distances))}")
    print(f"Part 2: {part2((time2, distance2))}")
