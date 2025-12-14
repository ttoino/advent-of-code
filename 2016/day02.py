import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    btns = {
                                    (0, -2): '1',
                     (-1, -1): '2', (0, -1): '3', (1, -1): '4',
        (-2, 0): '5', (-1, 0): '6',  (0, 0): '7',  (0, 1): '8', (0, 2): '9',
                      (-1, 1): 'A',  (0, 1): 'B',  (1, 1): 'C',
                                     (0, 2): 'D',
    }
    btn = (-2, 0)
    
    for l in inf:
        for d in l.strip():
            match d:
                case "U":
                    if btn[1] - abs(btn[0]) != -2:
                        btn = btn[0], btn[1] - 1
                case "R":
                    if btn[0] + abs(btn[1]) != 2:
                        btn = btn[0] + 1, btn[1]
                case "D":
                    if btn[1] + abs(btn[0]) != 2:
                        btn = btn[0], btn[1] + 1
                case "L":
                    if btn[0] - abs(btn[1]) != -2:
                        btn = btn[0] - 1, btn[1]
        outf.write(btns[btn])
