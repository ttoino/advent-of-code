import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    p = re.compile(r"\[|\]")

    s = 0
    for ip in inf:
        supports = [False, True]
        for i, part in enumerate(p.split(ip.strip())):
            for a, b, c, d in mit.windowed(part, 4):
                if a == d and b == c and a != b:
                    supports[i % 2] = not (i % 2)

        s += supports[0] and supports[1]

    outf.write(str(s))
