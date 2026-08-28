import sys


maxs = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def parse(i: str) -> tuple[int, list[list[tuple[int, str]]]]:
    id, results = i.strip().split(': ')
    id = int(id.split(' ')[1])
    rounds = [
        [(int(count), color) for count, color in (rr.split(' ') for rr in r.split(', '))]
        for r in results.split('; ')
    ]
    return id, rounds


def part1(inp: list[tuple[int, list[list[tuple[int, str]]]]]) -> int:
    result = 0
    for id, rounds in inp:
        possible = True
        for r in rounds:
            for count, color in r:
                if count > maxs[color]:
                    possible = False
        if possible:
            result += id
    return result


def part2(inp: list[tuple[int, list[list[tuple[int, str]]]]]) -> int:
    result = 0
    for _, rounds in inp:
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for r in rounds:
            for count, color in r:
                counts[color] = max(count, counts[color])
        result += counts['red'] * counts['green'] * counts['blue']
    return result


if __name__ == "__main__":
    inp = list(map(parse, sys.stdin.readlines()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
