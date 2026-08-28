import sys
from collections import Counter, deque

closing_brackets = {")": 3, "]": 57, "}": 1197, ">": 25137}
opening_brackets = ("(", "[", "{", "<")
bracket_map = {")": "(", "]": "[", "}": "{", ">": "<"}

closing_brackets_p2 = (")", "]", "}", ">")
opening_brackets_p2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def error_score(line: str) -> int:
    brackets = deque()
    for bracket in line:
        if bracket in opening_brackets:
            brackets.append(bracket)
        if bracket in closing_brackets:
            if brackets.pop() != bracket_map[bracket]:
                return closing_brackets[bracket]
    return 0


def error_score_p2(line: str) -> int:
    brackets = deque()
    for bracket in line:
        if bracket in opening_brackets_p2:
            brackets.append(bracket)
        if bracket in closing_brackets_p2:
            if brackets.pop() != bracket_map[bracket]:
                return 0
    score = 0
    while len(brackets):
        score *= 5
        score += opening_brackets_p2[brackets.pop()]
    return score


def part1(inp: list[str]) -> int:
    scores = map(error_score, inp)
    return sum(x * y for x, y in Counter(scores).items())


def part2(inp: list[str]) -> int:
    scores = map(error_score_p2, inp)
    scores = sorted((s for s in scores if s))
    return scores[len(scores) // 2]


if __name__ == "__main__":
    inp = sys.stdin.read().splitlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
