import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from hashlib import md5
import heapq as hq

with open("input") as inf, open("part1.out", "w+") as outf:
    passcode = inf.readline().strip()

    heap = [(0, "")]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p.count("D") - p.count("U") == 3 and p.count("R") - p.count(
                "L") == 3:
            outf.write(p)
            exit()

        for di, c in zip("UDLR", md5(bytes(passcode + p, "ascii")).hexdigest()):
            if ord("b") <= ord(c) <= ord("f"):
                hq.heappush(heap, (d + 1, p + di))
