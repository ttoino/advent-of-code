import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from scipy.optimize import linprog, milp, LinearConstraint
import numpy as np


def score(amount, ingredients):
    return ft.reduce(
        lambda x, y: x * y if y > 0 else 0,
        (sum(a * v for a, v in zip(amount, i)) for i in zip(*ingredients)), 1)


def brute_force_amounts(ingredients, ub, amount) -> list[list[int]]:
    if ingredients == 1:
        return [amount + [ub]]
    else:
        return sum((brute_force_amounts(ingredients - 1, ub - i, amount + [i])
                    for i in range(ub + 1)),
                   start=[])


with open("input") as inf, open("part1.out", "w+") as outf:
    ingredients = [(int(i[2].removesuffix(",")), int(i[4].removesuffix(",")),
                    int(i[6].removesuffix(",")), int(i[8].removesuffix(",")))
                   for i in map(lambda i: i.split(), inf)]

    outf.write(
        str(
            max(
                map(lambda x: score(x, ingredients),
                    brute_force_amounts(len(ingredients), 100, [])))))
