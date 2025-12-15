import sys
import itertools as it
from collections import deque


def solve(inp: list[str]) -> tuple[int, int]:
    width = len(inp[0])
    maze = "".join(inp)

    points = {c: (i % width, i // width, {}) for i, c in enumerate(maze) if c.isdigit()}

    for c, (x, y, dists) in points.items():
        q = deque([(0, (x, y))])
        visited = set()

        while len(q) > 0:
            d, p = q.pop()
            c = maze[p[0] + p[1] * width]

            if p in visited or c == "#":
                continue

            visited.add(p)

            if c.isdigit():
                dists[c] = d

            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                q.appendleft((d + 1, (p[0] + dx, p[1] + dy)))

    return min(
        sum(points[a][2][b] for a, b in it.pairwise(p))
        for p in it.permutations(points.keys())
    ), min(
        sum(points[a][2][b] for a, b in it.pairwise(("0", *p, "0")))
        for p in it.permutations(set(points.keys()) - {"0"})
    )


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    part1, part2 = solve(inp)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
