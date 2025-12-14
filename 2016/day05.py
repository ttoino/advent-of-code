import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from hashlib import md5

with open("input") as inf, open("part2.out", "w+") as outf:
    password = list("________")
    id = inf.readline().strip()

    for i in it.count():
        if (h := md5(bytes(f"{id}{i}",
                           encoding="ascii")).hexdigest()).startswith("00000"):
            pos = h[5]
            if pos.isdigit() and (pos := int(pos)) < 8 and password[pos] == "_":
                password[pos] = h[6]
                if "_" not in password:
                    outf.write("".join(password))
                    break
