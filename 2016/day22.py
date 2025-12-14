import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    nodes = [tuple(i.strip().split()) for i in list(inf)[2:]]
    pairs = [(a, b)
             for a, b in it.permutations(nodes, 2)
             if a[2] != "0T" and int(a[2][:-1]) <= int(b[3][:-1])]
    outf.write(str(len(pairs)))
