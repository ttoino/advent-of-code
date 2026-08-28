import functools as ft
import itertools as it
import operator as op
import sys


def path(x1, y1, x2, y2):
    if x1 == x2:
        return map(lambda y: (x1, y), range(min(y1, y2), max(y1, y2) + 1))
    elif y1 == y2:
        return map(lambda x: (x, y1), range(min(x1, x2), max(x1, x2) + 1))


def sum_tuples(*t):
    return ft.reduce(lambda x, y: tuple((i + j for i, j in zip(x, y))), t)


def parse(s: str) -> list[list[tuple[int, int]]]:
    return [
        [tuple(map(int, j.split(","))) for j in i.split(" -> ")]
        for i in s.splitlines()
    ]


def part1(inp: list[list[tuple[int, int]]]):
    paths = inp
    rocks = set()
    sand = set()
    current_grain = (500, 0)
    for p in paths:
        for (x1, y1), (x2, y2) in it.pairwise(p):
            rocks.update(set(path(x1, y1, x2, y2)))
    min_x = min(map(op.itemgetter(0), rocks)) - 5
    max_x = max(map(op.itemgetter(0), rocks)) + 5
    min_y = 0
    max_y = max(map(op.itemgetter(1), rocks)) + 5
    while True:
        next_pos = (current_grain[0], current_grain[1] + 1)
        if next_pos in rocks | sand:
            next_pos = (next_pos[0] - 1, next_pos[1])
            if next_pos in rocks | sand:
                next_pos = (next_pos[0] + 2, next_pos[1])
                if next_pos in rocks | sand:
                    sand.add(current_grain)
                    next_pos = (500, 0)
        current_grain = next_pos
        if current_grain[1] > max_y:
            return len(sand)


def part2(inp: list[list[tuple[int, int]]]):
    paths = inp
    rocks = set()
    sand = set()
    for p in paths:
        for (x1, y1), (x2, y2) in it.pairwise(p):
            rocks.update(set(path(x1, y1, x2, y2)))
    min_x = min(map(op.itemgetter(0), rocks)) - 100
    max_x = max(map(op.itemgetter(0), rocks)) + 100
    min_y = 0
    max_y = max(map(op.itemgetter(1), rocks)) + 2
    for x in range(min_x - 500, max_x + 500):
        rocks.add((x, max_y))
    while True:
        current_pos = (500, 0)
        to_add = set()
        obstacles = sand | rocks
        while True:
            to_add.add(current_pos)
            if (next_pos := sum_tuples(current_pos, (0, 1))) not in obstacles:
                to_add.clear()
                current_pos = next_pos
            elif (
                next_pos := sum_tuples(current_pos, (-1, 1))
            ) not in obstacles:
                if sum_tuples(current_pos, (1, 1)) not in obstacles:
                    to_add.clear()
                current_pos = next_pos
            elif (
                next_pos := sum_tuples(current_pos, (1, 1))
            ) not in obstacles:
                current_pos = next_pos
            else:
                break
        sand.update(to_add)
        if (500, 0) in sand:
            return len(sand)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
