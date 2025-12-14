import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from intervaltree import IntervalTree

with open("input") as inf, open("part1.out", "w+") as outf:
    tree = IntervalTree()
    tree[0:4294967296] = 1

    for i in inf:
        s, e = map(int, i.strip().split("-"))
        tree.chop(s, e + 1)

    outf.write(str(tree.begin()))
