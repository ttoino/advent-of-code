import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    s = inf.readline().strip()
    r = 0

    while "(" in s:
        ms, me = s.find("("), s.find(")")
        r += ms
        chars, times = map(int, s[ms + 1:me].split("x"))
        s = s[me + 1:me + chars + 1] * times + s[me + chars + 1:]

    r += len(s)

    outf.write(str(r))
