import sys
import re


def part1(inp: list[str]):
    return len(
        list(
            w
            for w in inp
            if "ab" not in w
            and "cd" not in w
            and "pq" not in w
            and "xy" not in w
            and re.search(r"(\w)\1", w)
            and len(re.findall(r"[aeiou]", w)) >= 3
        )
    )


def part2(inp: list[str]):
    return len(
        list(
            w for w in inp if re.search(r"(\w\w)\w*\1", w) and re.search(r"(\w)\w\1", w)
        )
    )


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
