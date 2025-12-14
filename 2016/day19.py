import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    n = f"{int(inf.readline().strip()):b}"
    outf.write(str(int(n[1:] + n[0], 2)))
