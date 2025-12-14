import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    pattern = re.compile(r"((?:\w+-)+)(\d+)\[(\w{5})\]")

    s = 0
    for i in inf:
        m = pattern.match(i)
        cs = "".join(
            sorted({c for c in m[1] if c != "-"},
                   key=lambda x: (-m[1].count(x), x))[:5])
        if cs == m[3]:
            s += int(m[2])

    outf.write(str(s))
