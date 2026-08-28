import more_itertools as mit


def part1(inp: str) -> int:
    return sum((int(a) for a, b, *c in mit.circular_shifts(inp) if a == b))


def part2(inp: str) -> int:
    l = inp
    return sum(
        (
            int(a)
            for a, b in zip(l, l[len(l) // 2 :] + l[: len(l) // 2])
            if a == b
        )
    )


if __name__ == "__main__":
    inp = input().strip()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
