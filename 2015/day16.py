import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    target_sue = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    sues = {
        int(i[1].removesuffix(":")): {
            k.removesuffix(":"): int(v.removesuffix(","))
            for k, v in mit.chunked(i[2:], 2)
        } for i in map(lambda i: i.split(), inf)
    }

    for i, sue in list(sues.items()):
        for k, v in target_sue.items():
            if k in sue and sue[k] != v:
                del sues[i]
                break

    outf.write(str(next(iter(sues))))
