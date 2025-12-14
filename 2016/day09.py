import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    s = inf.readline().strip()
    p = re.compile(r"(.*?)\((\d+)x(\d+)\)(.*)")
    r = ""

    while m := p.match(s):
        r += m[1]
        chars = int(m[2])
        times = int(m[3])
        r += m[4][:chars] * times
        s = m[4][chars:]

    r += s

    outf.write(str(len(r)))
