from curses.ascii import isalpha
import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

d = {}


class Literal():

    def __init__(self, v: str) -> None:
        self.v = int(v)

    @ft.cache
    def __call__(self) -> int:
        return self.v


class Passthrough():

    def __init__(self, v: str) -> None:
        self.v = v

    @ft.cache
    def __call__(self) -> int:
        return d[self.v]()


class Not():

    def __init__(self, v: str) -> None:
        self.v = v.split()[1]

    @ft.cache
    def __call__(self) -> int:
        return ~d[self.v]()


class And():

    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        if self.a.isalpha():
            a = d[self.a]()
        else:
            a = int(self.a)

        return a & d[self.b]()


class Or():

    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() | d[self.b]()


class Lshift():

    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() << int(self.b)


class Rshift():

    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() >> int(self.b)


with open("input") as inf, open("part1.out", "w+") as outf:

    for i in inf:
        i, o = i.strip().split(" -> ")

        if i.isdigit():
            d[o] = Literal(i)
        elif "NOT " in i:
            d[o] = Not(i)
        elif " AND " in i:
            d[o] = And(i)
        elif " OR " in i:
            d[o] = Or(i)
        elif " LSHIFT " in i:
            d[o] = Lshift(i)
        elif " RSHIFT " in i:
            d[o] = Rshift(i)
        else:
            d[o] = Passthrough(i)

    outf.write(str(d["a"]()))
