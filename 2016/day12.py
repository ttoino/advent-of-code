import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    instructions = [i.strip().split() for i in inf]
    registers = {c: 0 for c in "abcd"}
    registers["c"] = 1
    ip = 0

    while 0 <= ip < len(instructions):
        match instructions[ip]:
            case ["cpy", x, y]:
                registers[y] = registers[x] if x in "abcd" else int(x)
            case ["inc", x]:
                registers[x] += 1
            case ["dec", x]:
                registers[x] -= 1
            case ["jnz", x, y]:
                if (registers[x] if x in "abcd" else int(x)) != 0:
                    ip += int(y)
                    continue

        ip += 1
    
    outf.write(str(registers["a"]))
