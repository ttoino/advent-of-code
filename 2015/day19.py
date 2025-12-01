import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    replacements, molecule = "".join(inf).split("\n\n")
    molecule = molecule.strip()
    replacements = [s.split(" => ") for s in replacements.strip().splitlines()]
    s = set()

    for a, b in replacements:
        i = -1
        while (i := molecule.find(a, i + 1)) != -1:
            s.add(molecule[:i] + molecule[i:].replace(a, b, 1))

    outf.write(str(len(s)))
