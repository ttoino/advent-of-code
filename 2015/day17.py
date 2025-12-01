import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def brute_force(capacities, ub) -> int:
    if ub == 0:
        return 1

    if ub < 0 or len(capacities) == 0:
        return 0

    return brute_force(capacities[1:], ub - capacities[0]) + brute_force(
        capacities[1:], ub)


with open("input") as inf, open("part1.out", "w+") as outf:
    capacities = [int(i) for i in inf]
    outf.write(str(brute_force(capacities, 150)))
