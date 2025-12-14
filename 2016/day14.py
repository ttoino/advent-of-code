from hashlib import md5
import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


@ft.cache
def hash(salt, i):
    h = f"{salt}{i}"
    for _ in range(2017):
        h = md5(bytes(h, "ascii")).hexdigest()
    return h


with open("input") as inf, open("part2.out", "w+") as outf:
    salt = inf.readline().strip()
    p = re.compile(r"(.)\1\1")

    count = 0
    for i in it.count():
        if (m := p.search(hash(salt, i))) is not None and any(
            (m.group(1) * 5) in hash(salt, i + j) for j in range(1, 1001)):
            count += 1

            if count == 64:
                outf.write(str(i))
                break