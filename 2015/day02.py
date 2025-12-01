import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    s = 0

    for i in inf:
        i = sorted(map(int, i.split("x")))
        l, w, h = i

        s += l + l + w + w + l * w * h

    outf.write(str(s))
