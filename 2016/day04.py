import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from string import ascii_lowercase

with open("input") as inf, open("part2.out", "w+") as outf:
    pattern = re.compile(r"((?:\w+-)+)(\d+)\[(\w{5})\]")

    for i in inf:
        m = pattern.match(i)

        s = int(m[2])
        name = "".join(
            " " if c == "-" else ascii_lowercase[(ascii_lowercase.index(c) +
                                                  s) % 26] for c in m[1][:-1])

        if "north" in name:
            print(name)
            outf.write(m[2])
