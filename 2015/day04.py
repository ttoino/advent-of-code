import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from hashlib import md5

with open("input") as inf, open("part2.out", "w+") as outf:
    inp = inf.readline().strip()

    for i in it.count():
        if md5(bytes(f"{inp}{i}",
                     encoding="ascii")).hexdigest().startswith("000000"):
            outf.write(str(i))
            break