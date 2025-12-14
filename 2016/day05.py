import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from hashlib import md5

with open("input") as inf, open("part1.out", "w+") as outf:
    n = 0
    id = inf.readline().strip()

    for i in it.count():
        if (h := md5(bytes(f"{id}{i}",
                           encoding="ascii")).hexdigest()).startswith("00000"):
            outf.write(h[5])
            if (n := n + 1) == 8:
                break
