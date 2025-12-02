import sys


def magic_missile(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
):
    return (
        spent_mana + 53,
        boss_hp - 4,
        boss_damage,
        hp,
        mana - 53,
        shield,
        poison,
        recharge,
    )


def drain(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
):
    return (
        spent_mana + 73,
        boss_hp - 2,
        boss_damage,
        hp + 2,
        mana - 73,
        shield,
        poison,
        recharge,
    )


def shield(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
):
    if shield > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 113, boss_hp, boss_damage, hp, mana - 113, 6, poison, recharge


def poison(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
):
    if poison > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 173, boss_hp, boss_damage, hp, mana - 173, shield, 6, recharge


def recharge(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
):
    if recharge > 0:
        return 0, 0, 0, 0, 0, 0, 0, 0
    return spent_mana + 229, boss_hp, boss_damage, hp, mana - 229, shield, poison, 5


spells = [magic_missile, drain, shield, poison, recharge]


def simulate(
    spent_mana: int,
    boss_hp: int,
    boss_damage: int,
    hp: int,
    mana: int,
    shield: int,
    poison: int,
    recharge: int,
    part: int,
):
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
        simulate(
            *spell(
                spent_mana,
                boss_hp,
                boss_damage,
                hp - part + 1,
                mana,
                shield,
                poison,
                recharge,
            ),
            part,
        )
        for spell in spells
    )


def solve(boss_hp: int, boss_damage: int, hp: int, mana: int, part: int):
    return min(
        simulate(*spell(0, boss_hp, boss_damage, hp - part + 1, mana, 0, 0, 0), part)
        for spell in spells
    )


if __name__ == "__main__":
    boss_hp, boss_damage = tuple(
        int(i.strip().split(": ")[1]) for i in sys.stdin.readlines()
    )
    hp = 50
    mana = 500

    print(f"Part 1: {solve(boss_hp, boss_damage, hp, mana, 1)}")
    print(f"Part 2: {solve(boss_hp, boss_damage, hp, mana, 2)}")
