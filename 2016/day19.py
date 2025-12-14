import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    n = int(inf.readline().strip())
    r = 1
    s = -1

    for i in range(1, n):
        if r == i:
            r = 1
            s += 1
        else:
            r += 1 + (r >= 3**s)

    outf.write(str(r))
