import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            len(
                list(w for w in inf
                     if "ab" not in w and "cd" not in w and "pq" not in w and
                     "xy" not in w and re.search(r"(\w)\1", w) and
                     len(re.findall(r"[aeiou]", w)) >= 3))))
