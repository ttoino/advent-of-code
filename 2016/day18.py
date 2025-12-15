import sys
import more_itertools as mit


def solve(inp: list[tuple[bool, ...]], part2: bool) -> int:
    size = 400000 if part2 else 40
    while len(inp) < size:
        inp.append(
            tuple(
                not (
                    (not l and not c and r)
                    or (l and not c and not r)
                    or (not l and c and r)
                    or (l and c and not r)
                )
                for l, c, r in mit.triplewise((True, *inp[-1], True))
            )
        )

    return sum(sum(i) for i in inp)


if __name__ == "__main__":
    inp = [tuple(c == "." for c in sys.stdin.readlines())]

    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
