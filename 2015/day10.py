import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    pattern = re.compile(r"(\d)\1*")
    n = inf.readline()

    for i in range(50):
        print(f"\r{i}/50", flush=True, end="")

        nn = ""

        while m := pattern.match(n):
            nn += str(len(m[0])) + m[1]
            n = n.removeprefix(m[0])

        n = nn

    outf.write(str(len(n)))
