import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write("".join(
        Counter(a).most_common()[-1][0]
        for a in zip(*(i.strip() for i in inf))))
