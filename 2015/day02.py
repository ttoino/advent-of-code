import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    s = 0

    for i in inf:
        i = sorted(map(int, i.split("x")))
        l, w, h = i

        s += 3 * l * w + 2 * w * h + 2 * h * l

    outf.write(str(s))
