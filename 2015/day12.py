import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from json import load

def visit(o) -> int:
    match o:
        case int(o):
            return o
        case dict(o):
            return 0 if "red" in o.values() else sum(map(visit, o.values()))
        case list(o):
            return sum(map(visit, o))
        case _:
            return 0

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(str(visit(load(inf))))
