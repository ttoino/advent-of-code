import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    map = [tuple(c == "." for c in inf.readline().strip())]

    while len(map) < 40:
        map.append(
            tuple(not ((not l and not c and r) or (l and not c and not r) or
                       (not l and c and r) or (l and c and not r))
                  for l, c, r in mit.triplewise((True, *map[-1], True))))

    outf.write(str(sum(sum(i) for i in map)))
