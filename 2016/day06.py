from collections import Counter
import sys


def solve(inp: list[str], part2: bool) -> str:
    return "".join(Counter(a).most_common()[-1 if part2 else 0][0] for a in zip(*inp))


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
