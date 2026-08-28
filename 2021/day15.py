import heapq
import sys

offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def part1(inp: list[list[int]]) -> int:
    grid = [list(line) for line in inp]
    width = len(grid)
    height = len(grid[0])
    heap = [(0, 0, 0)]
    heapq.heapify(heap)
    visited = set()
    while len(heap):
        c, x, y = heapq.heappop(heap)
        if x == width - 1 and y == height - 1:
            return c
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in offsets:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < width and 0 <= ny < height:
                heapq.heappush(heap, (c + grid[nx][ny], nx, ny))


def part2(inp: list[list[int]]) -> int:
    grid = [list(line) for line in inp]
    ogrid = [[x for x in l] for l in grid]
    for i in range(1, 5):
        grid = [
            l + [x + i if x + i < 10 else (x + i + 1) % 10 for x in ogrid[j]]
            for j, l in enumerate(grid)
        ]
    ogrid = [[x for x in l] for l in grid]
    for i in range(1, 5):
        grid += [
            [x + i if x + i < 10 else (x + i + 1) % 10 for x in l]
            for l in ogrid
        ]
    width = len(grid)
    height = len(grid[0])
    heap = [(0, 0, 0)]
    heapq.heapify(heap)
    visited = set()
    while len(heap):
        c, x, y = heapq.heappop(heap)
        if x == width - 1 and y == height - 1:
            return c
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in offsets:
            nx, ny = (x + dx, y + dy)
            if 0 <= nx < width and 0 <= ny < height:
                heapq.heappush(heap, (c + grid[nx][ny], nx, ny))


if __name__ == "__main__":
    inp = [[int(x) for x in l.strip()] for l in sys.stdin]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
