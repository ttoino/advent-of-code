import itertools as it


def solve(data: str, part2: bool) -> str:
    size = 35651584 if part2 else 272

    while len(data) < size:
        data += "0" + "".join("1" if c == "0" else "0" for c in data[::-1])

    data = data[:size]

    while len(data) % 2 == 0:
        data = "".join(str(int(a == b)) for a, b in it.batched(data, 2))

    return data


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
