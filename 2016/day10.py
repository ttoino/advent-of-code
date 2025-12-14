import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


class Robot():
    number: str = None
    give_low_to: str = None
    give_high_to: str = None
    v1: int = None
    v2: int = None

    def __init__(self, n):
        self.number = n

    def ready(self):
        return self.give_high_to is not None and self.give_low_to is not None and self.v1 is not None and self.v2 is not None

    def handle(self):
        if (self.v1, self.v2) == (61, 17) or (self.v1, self.v2) == (17, 61):
            out(self.number)

        robots.setdefault(self.give_low_to, Robot(self.give_low_to))
        robots[self.give_low_to].give_value(min(self.v1, self.v2))
        robots.setdefault(self.give_high_to, Robot(self.give_high_to))
        robots[self.give_high_to].give_value(max(self.v1, self.v2))

    def give_value(self, v: int):
        if self.v1 is None:
            self.v1 = v
        else:
            self.v2 = v

        if self.ready():
            self.handle()

    def set_low(self, r: str):
        self.give_low_to = r

        if self.ready():
            self.handle()

    def set_high(self, r: str):
        self.give_high_to = r

        if self.ready():
            self.handle()


robots: dict[str, Robot] = {}

with open("input") as inf, open("part1.out", "w+") as outf:
    global out
    out = outf.write

    for i in inf:
        match i.strip().split():
            case ["value", x, "goes", "to", "bot", y]:
                robots.setdefault(y, Robot(y))
                robots[y].give_value(int(x))
            case ["bot", x, "gives", "low", "to", obl, y, "and", "high", "to", obh, z]:
                robots.setdefault(x, Robot(x))

                if obl == "bot":
                    robots[x].set_low(y)

                if obh == "bot":
                    robots[x].set_high(z)
