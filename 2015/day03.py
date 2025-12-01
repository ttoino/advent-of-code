import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    s = {(0, 0)}
    curr = (0, 0)

    for d in inf.readline():
        match d:
            case '>':
                curr = curr[0] + 1, curr[1]
            case '<':
                curr = curr[0] - 1, curr[1]
            case '^':
                curr = curr[0], curr[1] + 1
            case 'v':
                curr = curr[0], curr[1] - 1
        s.add(curr)

    outf.write(str(len(s)))
