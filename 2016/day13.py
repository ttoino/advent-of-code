import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
import heapq as hq


@ft.cache
def is_wall(x, y, n):
    return f"{x*x + 3*x + 2*x*y + y + y*y + n:b}".count("1") % 2


with open("input") as inf, open("part1.out", "w+") as outf:
    n = int(inf.readline().strip())

    visited = set()
    heap = [(0, (1, 1))]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p in visited:
            continue

        visited.add(p)

        if p == (31, 39):
            outf.write(str(d))
            exit()

        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            if not is_wall(p[0] + dx, p[1] + dy, n):
                hq.heappush(heap, (d + 1, (p[0] + dx, p[1] + dy)))
