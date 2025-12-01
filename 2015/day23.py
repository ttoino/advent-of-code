import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    instructions = [re.split(r",? ", i.strip()) for i in inf]

    registers = { "a": 1, "b": 0 }
    ip = 0

    while 0 <= ip < len(instructions):
        match instructions[ip]:
            case ["hlf", r]:
                registers[r] //= 2
            case ["tpl", r]:
                registers[r] *= 3
            case ["inc", r]:
                registers[r] += 1
            case ["jmp", offset]:
                ip += int(offset)
                continue
            case ["jie", r, offset]:
                if registers[r] % 2 == 0:
                    ip += int(offset)
                    continue
            case ["jio", r, offset]:
                if registers[r] == 1:
                    ip += int(offset)
                    continue
        ip += 1

    outf.write(str(registers["b"]))
