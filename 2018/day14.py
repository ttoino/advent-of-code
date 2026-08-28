import sys


def part1(inp: int):
    n = inp
    scores = [3, 7]
    pos1 = 0
    pos2 = 1
    while len(scores) < n + 10:
        new_score = scores[pos1] + scores[pos2]
        scores.extend(map(int, str(new_score)))
        pos1 += 1 + scores[pos1]
        pos1 %= len(scores)
        pos2 += 1 + scores[pos2]
        pos2 %= len(scores)
    return "".join(map(str, scores[n:]))


def part2(inp: list[int]):
    n = inp
    scores = [3, 7]
    pos1 = 0
    pos2 = 1
    while True:
        new_score = map(int, str(scores[pos1] + scores[pos2]))
        scores.append(next(new_score))
        if scores[-len(n) :] == n:
            break
        if (x := next(new_score, None)) is not None:
            scores.append(x)
            if scores[-len(n) :] == n:
                break
        pos1 += 1 + scores[pos1]
        pos1 %= len(scores)
        pos2 += 1 + scores[pos2]
        pos2 %= len(scores)
    return len(scores) - len(n)


if __name__ == "__main__":
    line = sys.stdin.readline().strip()

    print(f"Part 1: {part1(int(line))}")
    print(f"Part 2: {part2(list(map(int, line)))}")
