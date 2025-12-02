import sys
import more_itertools as mit
import operator as op


def solve(sues: dict[int, dict[str, int]], part: int):
    target_sue = {
        "children": (3, op.ne),
        "cats": (7, op.le),
        "samoyeds": (2, op.ne),
        "pomeranians": (3, op.ge),
        "akitas": (0, op.ne),
        "vizslas": (0, op.ne),
        "goldfish": (5, op.ge),
        "trees": (3, op.le),
        "cars": (2, op.ne),
        "perfumes": (1, op.ne),
    }

    for i, sue in list(sues.items()):
        for k, (v, o) in target_sue.items():
            if k in sue and (
                (part == 1 and sue[k] != v) or (part == 2 and o(sue[k], v))
            ):
                del sues[i]
                break

    return next(iter(sues))


if __name__ == "__main__":
    sues = {
        int(i[1].removesuffix(":")): {
            k.removesuffix(":"): int(v.removesuffix(","))
            for k, v in mit.chunked(i[2:], 2)
        }
        for i in (i.split() for i in sys.stdin.readlines())
    }

    print(f"Part 1: {solve(sues.copy(), 1)}")
    print(f"Part 2: {solve(sues.copy(), 2)}")
