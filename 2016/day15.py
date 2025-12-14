import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

# Alternative solution: solve the system of modular equations of the type
#   t + n + p = 0 mod k
with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(
        r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)\.")
    discs = [tuple(map(int, (x for x in p.match(i).groups()))) for i in inf]
    discs += [(len(discs) + 1, 11, 0)]

    for t in it.count():
        b = True

        for n, k, p in discs:
            b &= (t + n + p) % k == 0

        if b:
            outf.write(str(t))
            exit()
