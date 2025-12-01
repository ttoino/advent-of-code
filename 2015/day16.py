import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    target_sue = {
        "children": (3, op.ne),
        "cats": (7, op.le),
        "samoyeds": (2, op.ne),
        "pomeranians": (3, op.ge),
        "akitas": (0, op.ne),
        "vizslas": (0, op.ne),
        "goldfish": (5, op.ge),
        "trees": (3, op.le),
        "cars": (2, op.ne),
        "perfumes": (1, op.ne)
    }

    sues = {
        int(i[1].removesuffix(":")): {
            k.removesuffix(":"): int(v.removesuffix(","))
            for k, v in mit.chunked(i[2:], 2)
        } for i in map(lambda i: i.split(), inf)
    }

    for i, sue in list(sues.items()):
        for k, (v, o) in target_sue.items():
            if k in sue and o(sue[k], v):
                del sues[i]
                break

    outf.write(str(next(iter(sues))))
