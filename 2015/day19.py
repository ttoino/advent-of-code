import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    replacements, molecule = "".join(inf).split("\n\n")
    molecule = molecule.strip()

    # All replacements are of the following types
    #   - µ => αβ
    #   - µ => αRnβAr
    #   - µ => αRnβYγAr
    #   - µ => αRnβYγYδAr
    # All types produce an additional atom.
    # Rn and Ar only show up on the right hand side and always in pairs, so they
    #  can be ignored.
    # Y always shows up on the right hand side, between an Rn and an Ar and for
    #  every Y there is another atom, so we can ignore these.
    # This gives us the expression
    #   #atoms - #Rn - #Ar - 2×#Y - 1
    # (- 1 because we start with a symbol, e)
    outf.write(
        str(
            len(re.findall(r"[A-Z]", molecule)) - molecule.count("Rn") -
            molecule.count("Ar") - 2 * molecule.count("Y") - 1))
