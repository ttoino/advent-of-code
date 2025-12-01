import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def get_group(weights, remaining, groups, target):
    for i in range(1, len(weights)):
        for c in sorted(
            (c for c in it.combinations(weights, i) if sum(c) == target),
                key=lambda x: ft.reduce(op.mul, x)):
            if remaining == 2:
                return True
            if remaining < groups:
                return get_group(weights - set(c), remaining - 1, groups,
                                 target)

            return ft.reduce(op.mul, c)


with open("input") as inf, open("part2.out", "w+") as outf:
    weights = {int(i.strip()) for i in inf}
    groups = 4

    outf.write(str(get_group(weights, groups, groups, sum(weights) // groups)))
