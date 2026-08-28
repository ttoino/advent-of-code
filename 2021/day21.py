import functools as ft
import itertools as it
import sys


@ft.cache
def dirac(p1p, p2p, p1s, p2s, isp1):
    if p1s > 20 or p2s > 20:
        return (int(p1s > 20), int(p2s > 20))
    rp1, rp2 = (0, 0)
    for roll in map(sum, it.product(range(1, 4), range(1, 4), range(1, 4))):
        if isp1:
            np1p = (p1p + roll) % 10
            np1s = p1s + np1p + 1
            p1, p2 = dirac(np1p, p2p, np1s, p2s, not isp1)
            rp1 += p1
            rp2 += p2
        else:
            np2p = (p2p + roll) % 10
            np2s = p2s + np2p + 1
            p1, p2 = dirac(p1p, np2p, p1s, np2s, not isp1)
            rp1 += p1
            rp2 += p2
    return (rp1, rp2)


def part1(inp: tuple[int, int]) -> int:
    p1_pos, p2_pos = inp
    p1_score = 0
    p2_score = 0
    die = it.cycle(range(1, 101))
    die_count = 0
    is_p1_turn = True
    while p1_score < 1000 and p2_score < 1000:
        if is_p1_turn:
            p1_pos = (p1_pos + next(die) + next(die) + next(die)) % 10
            p1_score += p1_pos + 1
        else:
            p2_pos = (p2_pos + next(die) + next(die) + next(die)) % 10
            p2_score += p2_pos + 1
        die_count += 3
        is_p1_turn = not is_p1_turn
    return die_count * (p2_score if p2_score < p1_score else p1_score)


def part2(inp: tuple[int, int]) -> int:
    p1p, p2p = inp
    return max(dirac(p1p, p2p, 0, 0, True))


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    inp = (int(lines[0].split()[-1]) - 1, int(lines[1].split()[-1]) - 1)

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
