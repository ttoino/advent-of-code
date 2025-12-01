import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def magic_missile(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison,
                  recharge):
    return spent_mana + 53, boss_hp - 4, boss_damage, hp, mana - 53, shield, poison, recharge


def drain(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison, recharge):
    return spent_mana + 73, boss_hp - 2, boss_damage, hp + 2, mana - 73, shield, poison, recharge


def shield(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison,
           recharge):
    if shield > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 113, boss_hp, boss_damage, hp, mana - 113, 6, poison, recharge


def poison(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison,
           recharge):
    if poison > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 173, boss_hp, boss_damage, hp, mana - 173, shield, 6, recharge


def recharge(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison,
             recharge):
    if recharge > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 229, boss_hp, boss_damage, hp, mana - 229, shield, poison, 5


spells = [magic_missile, drain, shield, poison, recharge]


def simulate(spent_mana, boss_hp, boss_damage, hp, mana, shield, poison,
             recharge):
    if hp <= 0 or mana <= 0:
        return 10000000000000

    shield -= 1
    boss_hp -= (poison > 0) * 3
    poison -= 1
    mana += (recharge > 0) * 101
    recharge -= 1

    if boss_hp <= 0:
        return spent_mana

    hp -= max(1, boss_damage - (shield > 0) * 7)

    if hp <= 0 or mana <= 0:
        return 10000000000000

    shield -= 1
    boss_hp -= (poison > 0) * 3
    poison -= 1
    mana += (recharge > 0) * 101
    recharge -= 1

    if boss_hp <= 0:
        return spent_mana

    return min(
        simulate(*spell(spent_mana, boss_hp, boss_damage, hp -
                        1, mana, shield, poison, recharge)) for spell in spells)


with open("input") as inf, open("part2.out", "w+") as outf:
    boss_hp, boss_damage = tuple(int(i.strip().split(": ")[1]) for i in inf)
    hp = 50
    mana = 500

    outf.write(
        str(
            min(
                simulate(*spell(0, boss_hp, boss_damage, hp - 1, mana, 0, 0, 0))
                for spell in spells)))
