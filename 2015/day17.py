import sys


def brute_force(capacities, ub, amount=0) -> list[int]:
    if ub == 0:
        return [amount]

    if ub < 0 or len(capacities) == 0:
        return []

    return brute_force(capacities[1:], ub - capacities[0], amount + 1) + brute_force(
        capacities[1:], ub, amount
    )


if __name__ == "__main__":
    capacities = [int(i) for i in sys.stdin.readlines()]

    r = brute_force(capacities, 150)

    part1 = len(r)
    part2 = r.count(min(r))

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
