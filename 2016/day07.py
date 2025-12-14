import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(r"\[|\]")

    s = 0
    for ip in inf:
        ss, hs = mit.partition(lambda x: x[0] % 2,
                               enumerate(p.split(ip.strip())))
        abas = [(a, b, c)
                for _, s in ss
                for a, b, c in mit.triplewise(s)
                if a == c and b != a]

        s += any("".join((b, a, b)) in s for _, s in hs for a, b, a in abas)

    outf.write(str(s))
