import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    reindeer = [(int(i[3]), int(i[6]), int(i[13]))
                for i in map(lambda i: i.split(), inf)]
    dists = [0 for i in range(len(reindeer))]
    rest = [-t for _, t, _ in reindeer]

    for _ in range(2503):
        for i, (s, t, r) in enumerate(reindeer):
            if rest[i] < 0:
                dists[i] += s
            rest[i] += 1
            if rest[i] == r:
                rest[i] = -t

    outf.write(str(max(dists)))
