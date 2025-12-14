import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(
                ft.reduce(op.and_, (p[0] + p[1] > p[2]
                                    for p in it.permutations(i)))
                for i in (map(int,
                              i.strip().split()) for i in inf))))
