import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, deque

with open("input") as inf, open("part2.out", "w+") as outf:
    maze = [i.strip() for i in inf]
    width, height = len(maze[0]), len(maze)
    maze = list("".join(maze))

    points = {
        c: (i % width, i // width, {})
        for i, c in enumerate(maze)
        if c.isdigit()
    }

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

    outf.write(
        str(
            min(
                sum(points[a][2][b]
                    for a, b in it.pairwise(('0', *p, '0')))
                for p in it.permutations(set(points.keys()) - {'0'}))))
