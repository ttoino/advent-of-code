import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    floor = 0
    for i, c in enumerate(inf.readline()):
        floor += c == "("
        floor -= c == ")"
        if floor == -1:
            outf.write(str(i + 1))
            break
