import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            len(
                list(w for w in inf if re.search(r"(\w\w)\w*\1", w) and
                     re.search(r"(\w)\w\1", w)))))
