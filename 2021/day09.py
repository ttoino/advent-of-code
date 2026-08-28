import sys

import functools as ft
import itertools as it
import operator as op


height_map = None
w = 0
h = 0
visited_pos = set()


def is_localmin(hm: tuple[tuple[int, ...], ...], pos, size):
    x, y = pos
    w, h = size
    for dx, dy in it.product(range(-1, 2), range(-1, 2)):
        nx, ny = (x + dx, y + dy)
        if 0 <= nx < w and 0 <= ny < h and (hm[ny][nx] < hm[y][x]):
            return False
    return True


def visit(x, y):
    if x >= w or x < 0 or y >= h or (y < 0) or ((x, y) in visited_pos):
        return 0
    v = height_map[y][x]
    visited_pos.add((x, y))
    if v == 9:
        return 0
    return 1 + visit(x + 1, y) + visit(x - 1, y) + visit(x, y + 1) + visit(x, y - 1)


def part1(inp: tuple[tuple[int, ...], ...]) -> int:
    height_map = inp
    size = (len(height_map[0]), len(height_map))
    return sum(
        v + 1
        for y, line in enumerate(height_map)
        for x, v in enumerate(line)
        if is_localmin(height_map, (x, y), size)
    )


def part2(inp: tuple[tuple[int, ...], ...]) -> int:
    global height_map, w, h
    height_map = inp
    w, h = (len(height_map[0]), len(height_map))
    areas = sorted((visit(x, y) for x, y in it.product(range(w), range(h))))
    return ft.reduce(op.mul, areas[-3:], 1)


if __name__ == "__main__":
    inp = tuple(tuple(map(int, line.strip())) for line in sys.stdin)

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
