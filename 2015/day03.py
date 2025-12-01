import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    s = {(0, 0)}
    curr = (0, 0)
    curr_r = (0, 0)

    for i, d in enumerate(inf.readline()):
        match d:
            case '>':
                if i % 2:
                    curr = curr[0] + 1, curr[1]
                else:
                    curr_r = curr_r[0] + 1, curr_r[1]
            case '<':
                if i % 2:
                    curr = curr[0] - 1, curr[1]
                else:
                    curr_r = curr_r[0] - 1, curr_r[1]
            case '^':
                if i % 2:
                    curr = curr[0], curr[1] + 1
                else:
                    curr_r = curr_r[0], curr_r[1] + 1
            case 'v':
                if i % 2:
                    curr = curr[0], curr[1] - 1
                else:
                    curr_r = curr_r[0], curr_r[1] - 1
        
        if i % 2:
            s.add(curr)
        else:
            s.add(curr_r)

    outf.write(str(len(s)))
