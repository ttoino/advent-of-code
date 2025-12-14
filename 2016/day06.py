import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from statistics import mode

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write("".join(mode(a) for a in zip(*(i.strip() for i in inf))))
