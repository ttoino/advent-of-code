import functools as ft
import sys

d = {}


class Literal:
    def __init__(self, v: str) -> None:
        self.v = int(v)

    @ft.cache
    def __call__(self) -> int:
        return self.v


class Passthrough:
    def __init__(self, v: str) -> None:
        self.v = v

    @ft.cache
    def __call__(self) -> int:
        return d[self.v]()


class Not:
    def __init__(self, v: str) -> None:
        self.v = v.split()[1]

    @ft.cache
    def __call__(self) -> int:
        return ~d[self.v]()


class And:
    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        if self.a.isalpha():
            a = d[self.a]()
        else:
            a = int(self.a)

        return a & d[self.b]()


class Or:
    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() | d[self.b]()


class Lshift:
    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() << int(self.b)


class Rshift:
    def __init__(self, v: str) -> None:
        self.a, _, self.b = v.split()

    @ft.cache
    def __call__(self) -> int:
        return d[self.a]() >> int(self.b)


def solve(inp: list[tuple[str, str]], a=None):
    d.clear()

    for i, o in inp:
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

    if a:
        d["b"] = Literal(a)

    return d["a"]()


if __name__ == "__main__":
    inp: list[tuple[str, str]] = [
        tuple(i.strip().split(" -> ")) for i in sys.stdin.readlines()
    ]

    part1 = solve(inp)
    part2 = solve(inp, part1)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
