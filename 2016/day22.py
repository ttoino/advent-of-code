import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(r"-[xy]|[T%]?\s+")
    nodes = sorted((tuple(map(int,
                              p.split(i.strip()[:-1])[1:]))
                    for i in list(inf)[2:]),
                   key=lambda x: (x[1], x[0]))
    print("\n".join(" ".join(
        "!" if x == 0 and y == 0 else ("G" if x == 32 and y == 0 else (
            "#" if size > 400 else ("_" if used == 0 else ".")))
        for x, y, size, used, avail, percent in line)
                    for y, line in it.groupby(nodes, key=lambda x: x[1])))

    # Solve by hand
    outf.write(input())
