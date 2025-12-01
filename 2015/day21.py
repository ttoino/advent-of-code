import itertools as it
from math import ceil
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]

armor = [
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
]

rings = [
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
]


def generate_loadouts():
    return sorted(
        (ft.reduce(lambda x, y:
                   (x[0] + y[0], x[1] + y[1], x[2] + y[2]), [i, j, *k],
                   (0, 0, 0)) for i in weapons for j in armor
         for k in it.chain([[]], it.combinations(rings, 1),
                           it.combinations(rings, 2))),
        key=lambda x: -x[0])


def wins(loadout, boss):
    hp = 100
    price, damage, armor = loadout
    boss_hp, boss_damage, boss_armor = boss
    damage_to_boss = max(1, damage - boss_armor)
    damage_from_boss = max(1, boss_damage - armor)
    turns_to_die = ceil(hp / damage_from_boss)
    turns_to_kill = ceil(boss_hp / damage_to_boss)
    return turns_to_die > turns_to_kill - 1


with open("input") as inf, open("part2.out", "w+") as outf:
    boss = tuple(
        int(i.strip().split(": ")[1]) for i in inf)  # hp, damage, armor

    outf.write(str(next(
        i[0] for i in generate_loadouts() if not wins(i, boss))))
