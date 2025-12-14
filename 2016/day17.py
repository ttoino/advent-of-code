import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from hashlib import md5
import heapq as hq

with open("input") as inf, open("part2.out", "w+") as outf:
    passcode = inf.readline().strip()

    heap = [(0, "", 1, 1)]
    paths = set()

    while len(heap) > 0:
        d, p, x, y = hq.heappop(heap)

        if p.count("D") - p.count("U") == 3 and p.count("R") - p.count(
                "L") == 3:
            paths.add(p)
            continue

        for di, c in zip("UDLR", md5(bytes(passcode + p, "ascii")).hexdigest()):
            nx = x + (di == "R") - (di == "L")
            ny = y + (di == "D") - (di == "U")
            if 0 < nx <= 4 and 0 < ny <= 4 and ord("b") <= ord(c) <= ord("f"):
                hq.heappush(heap, (d + 1, p + di, nx, ny))

    outf.write(str(max(map(len, paths))))
