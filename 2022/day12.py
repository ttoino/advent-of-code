import sys

import functools as ft
import heapq as h



DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


grid = []
width = 0
height = 0


def sum_tuples(*t):
    return ft.reduce(lambda x, y: tuple((i + j for i, j in zip(x, y))), t)


def dijkstra(start: tuple[int, int], end: tuple[int, int]):
    heap = [(0, *start)]
    visited = set()
    while len(heap):
        dist, x, y = h.heappop(heap)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        val = ord(grid[y][x])
        if (x, y) == end:
            return dist
        for d in DIRS:
            new_x, new_y = sum_tuples((x, y), d)
            if new_x >= width or new_x < 0 or new_y >= height or (new_y < 0):
                continue
            new_val = ord(grid[new_y][new_x])
            if new_val - val <= 1:
                h.heappush(heap, (dist + 1, new_x, new_y))
    return 100000000000000


def parse(s: str) -> list[list[str]]:
    return [list(l) for l in s.splitlines()]


def part1(inp: list[list[str]]):
    grid = [row[:] for row in inp]
    start = (0, 0)
    end = (0, 0)
    width = len(grid[0])
    height = len(grid)
    for y, l in enumerate(grid):
        for x, i in enumerate(l):
            if i == 'S':
                start = (x, y)
                grid[y][x] = 'a'
            elif i == 'E':
                end = (x, y)
                grid[y][x] = 'z'
    heap = [(0, *start)]
    visited = set()
    while len(heap):
        dist, x, y = h.heappop(heap)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        val = ord(grid[y][x])
        if (x, y) == end:
            return dist
            break
        for d in DIRS:
            new_x, new_y = sum_tuples((x, y), d)
            if new_x >= width or new_x < 0 or new_y >= height or (new_y < 0):
                continue
            new_val = ord(grid[new_y][new_x])
            if new_val - val <= 1:
                h.heappush(heap, (dist + 1, new_x, new_y))


def part2(inp: list[list[str]]):
    global grid, width, height
    grid = [row[:] for row in inp]
    start = []
    end = (0, 0)
    width = len(grid[0])
    height = len(grid)
    for y, l in enumerate(grid):
        for x, i in enumerate(l):
            if i == 'S' or i == 'a':
                start.append((x, y))
                grid[y][x] = 'a'
            elif i == 'E':
                end = (x, y)
                grid[y][x] = 'z'
    return min((dijkstra(p, end) for p in start))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
