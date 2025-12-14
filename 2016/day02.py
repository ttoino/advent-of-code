import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    btn = 5
    
    for l in inf:
        for d in l.strip():
            match d:
                case "U":
                    if btn > 3:
                        btn -= 3
                case "R":
                    if btn % 3 != 0:
                        btn += 1
                case "D":
                    if btn < 7:
                        btn += 3
                case "L":
                    if btn % 3 != 1:
                        btn -= 1
        outf.write(str(btn))
