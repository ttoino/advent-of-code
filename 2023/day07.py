import sys
from collections import Counter

MAPPING = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

MAPPING_P2 = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def score(
    line: str, mapping: dict[str, int]
) -> tuple[int, int, int, int, int, int]:
    hand, _ = line.split()
    counts = Counter(hand)
    counts = sorted(counts.values(), reverse=True)
    best = counts[0]
    second = counts[1] if len(counts) > 1 else 0
    hand = [mapping[x] for x in hand]
    return (best, second, *hand)


def score_p2(line: str) -> tuple[int, int, int, int, int, int]:
    hand, _ = line.split()
    hand_without_jokers = hand.replace("J", "")
    counts = Counter(hand_without_jokers)
    counts = sorted(counts.values(), reverse=True)
    best = (counts[0] if len(counts) > 0 else 0) + hand.count("J")
    second = counts[1] if len(counts) > 1 else 0
    hand = [MAPPING_P2[x] for x in hand]
    return (best, second, *hand)


def part1(inp: list[str]) -> int:
    return sum(
        map(
            lambda x: int(x[1].split()[1]) * (x[0] + 1),
            enumerate(sorted(inp, key=lambda l: score(l, MAPPING))),
        )
    )


def part2(inp: list[str]) -> int:
    return sum(
        map(
            lambda x: int(x[1].split()[1]) * (x[0] + 1),
            enumerate(sorted(inp, key=score_p2)),
        )
    )


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
