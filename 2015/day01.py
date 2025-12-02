def part1(inp: str):
    return inp.count("(") - inp.count(")")


def part2(inp: str):
    floor = 0
    for i, c in enumerate(inp):
        floor += c == "("
        floor -= c == ")"
        if floor == -1:
            return i + 1


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
