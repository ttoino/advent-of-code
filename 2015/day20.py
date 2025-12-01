import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    t = int(inf.readline().strip()) // 10
    houses = list(0 for _ in range(t + 1))

    for i in range(1, t + 1):
        for j in range(i, t + 1, i):
            houses[j] += i

    outf.write(str(next(i for i, x in enumerate(houses) if x >= t)))
