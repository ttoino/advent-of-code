import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    inp = inf.readline()
    outf.write(str(inp.count("(") - inp.count(")")))
