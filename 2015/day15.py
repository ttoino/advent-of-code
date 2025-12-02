import sys
import functools as ft


def score(amount: list[int], ingredients: list[tuple[int, int, int, int]]):
    return ft.reduce(
        lambda x, y: x * y if y > 0 else 0,
        (sum(a * v for a, v in zip(amount, i)) for i in zip(*ingredients)),
        1,
    )


def calories(
    amount: list[int], ingredients: list[tuple[tuple[int, int, int, int], int]]
):
    return sum(a * c for a, (_, c) in zip(amount, ingredients))


def brute_force_amounts(
    ingredients: int, ub: int, amount: list[int]
) -> list[list[int]]:
    if ingredients == 1:
        return [amount + [ub]]
    else:
        return sum(
            (
                brute_force_amounts(ingredients - 1, ub - i, amount + [i])
                for i in range(ub + 1)
            ),
            start=[],
        )


def part1(ingredients: list[tuple[tuple[int, int, int, int], int]]):
    return max(
        score(x, next(zip(*ingredients)))
        for x in brute_force_amounts(len(ingredients), 100, [])
    )


def part2(ingredients: list[tuple[tuple[int, int, int, int], int]]):
    return max(
        score(x, next(zip(*ingredients)))
        for x in brute_force_amounts(len(ingredients), 100, [])
        if calories(x, ingredients) == 500
    )


if __name__ == "__main__":
    ingredients = [
        (
            (
                int(i[2].removesuffix(",")),
                int(i[4].removesuffix(",")),
                int(i[6].removesuffix(",")),
                int(i[8].removesuffix(",")),
            ),
            int(i[10].removesuffix(",")),
        )
        for i in (i.split() for i in sys.stdin.readlines())
    ]

    print(f"Part 1: {part1(ingredients)}")
    print(f"Part 2: {part2(ingredients)}")
