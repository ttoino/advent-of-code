import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

def solve(instructions, a):
    registers = {c: 0 for c in "abcd"}
    registers["a"] = a
    ip = 0
    transmission = []

    while 0 <= ip < len(instructions):
        match instructions[ip:ip+5]:
            case [
                ["inc", a],
                ["dec", c],
                ["jnz", c1, "-2"],
                ["dec", d],
                ["jnz", d1, "-5"]
            ] if c == c1 and d == d1:
                registers[a] += registers[c] * registers[d]
                ip += 5
                continue

        match instructions[ip]:
            case ["cpy", x, y]:
                if y in "abcd":
                    registers[y] = registers[x] if x in "abcd" else int(x)
            case ["inc", x]:
                registers[x] += 1
            case ["dec", x]:
                registers[x] -= 1
            case ["jnz", x, y]:
                if (registers[x] if x in "abcd" else int(x)) != 0:
                    ip += registers[y] if y in "abcd" else int(y)
                    continue
            case ["tgl", x]:
                x = registers[x] if x in "abcd" else int(x)
                if 0 <= ip + x < len(instructions):
                    i = instructions[ip + x][0]
                    instructions[ip + x][0] = "dec" if i == "inc" else ("inc" if i in ("dec", "tgl", "out") else ("cpy" if i == "jnz" else "jnz"))
            case ["out", x]:
                transmission.append(registers[x] if x in "abcd" else int(x))
                if len(transmission) >= 2 and transmission[-2:] not in ([0, 1], [1, 0]):
                    return False
                elif len(transmission) > 1000:
                    return True

        ip += 1

with open("input") as inf, open("part1.out", "w+") as outf:
    instructions = [i.strip().split() for i in inf]
    
    for i in it.count():
        print(i, end="\r")
        if solve(instructions, i):    
            outf.write(str(i))
            break
