import re
import sys

pattern = re.compile(
    r".*?(\d|one|two|three|four|five|six|seven|eight|nine)(?:.*(\d|one|two|three|four|five|six|seven|eight|nine))?.*?"
)

digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def part1(inp: list[str]) -> int:
    return sum(
        map(
            lambda l: int(
                (r := list(filter(lambda s: s.isdigit(), l)))[0] + r[-1]
            ),
            inp,
        )
    )


def part2(inp: list[str]) -> int:
    return sum(
        map(
            lambda l: int(
                digit_dict[(r := pattern.match(l))[1]]
                + digit_dict[r[2] or r[1]]
            ),
            inp,
        )
    )


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
