import itertools as it
from time import sleep
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
import heapq as hq

import os


@ft.cache
def is_wall(x, y, n):
    return f"{x*x + 3*x + 2*x*y + y + y*y + n:b}".count("1") % 2


with open("input") as inf, open("part2.out", "w+") as outf:
    n = int(inf.readline().strip())

    tw, th = os.get_terminal_size()

    print("\n".join("".join("#" if is_wall(x, y, n) else " "
                            for x in range(tw))
                    for y in range(th)),
          end="")

    visited = set()
    heap = [(0, (1, 1))]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p in visited or d > 50 or p[0] < 0 or p[1] < 0:
            continue

        print(f"\x1b[{p[1] + 1};{p[0] + 1}HO", end="", flush=True)
        sleep(.1)

        visited.add(p)

        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            if not is_wall(p[0] + dx, p[1] + dy, n):
                hq.heappush(heap, (d + 1, (p[0] + dx, p[1] + dy)))

    print(f"\x1b[{th};{1}H")

    outf.write(str(len(visited)))
