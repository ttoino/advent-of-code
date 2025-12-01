import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def brute_force(capacities, ub, amount=0) -> list[int]:
    if ub == 0:
        return [amount]

    if ub < 0 or len(capacities) == 0:
        return []

    return brute_force(capacities[1:], ub - capacities[0],
                       amount + 1) + brute_force(capacities[1:], ub, amount)


with open("input") as inf, open("part2.out", "w+") as outf:
    capacities = [int(i) for i in inf]
    r = brute_force(capacities, 150)
    outf.write(str(r.count(min(r))))
