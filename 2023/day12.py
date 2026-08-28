import itertools as it
import sys


def parse(i: str) -> tuple[str, list[int]]:
    springs, groups = i.split(" ")
    return springs, list(map(int, groups.split(",")))


def solve(inp: list[tuple[str, list[int]]]) -> int:
    result = 0
    for springs, groups in inp:
        unknown = springs.count("?")
        for replacements in tuple(it.product(*(".#",) * unknown)):
            replaced = springs
            for replacement in replacements:
                replaced = replaced.replace("?", replacement, 1)
            new_groups = []
            count = 0
            for s in replaced:
                if s == ".":
                    if count > 0:
                        new_groups.append(count)
                    count = 0
                else:
                    count += 1
            if count > 0:
                new_groups.append(count)
            if groups == new_groups:
                result += 1
    return result


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Solution: {solve(inp)}")
