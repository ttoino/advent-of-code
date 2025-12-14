import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    data = inf.readline().strip()

    while len(data) < 35651584:
        data += "0" + "".join("1" if c == "0" else "0" for c in data[::-1])

    data = data[:35651584]

    while len(data) % 2 == 0:
        data = "".join(str(int(a == b)) for a, b in mit.chunked(data, 2))

    outf.write(data)
