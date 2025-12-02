import re


def solve(inp: str, part: int):
    pattern = re.compile(r"(\d)\1*")
    n = inp

    for _ in range(40 if part == 1 else 50):
        nn = ""

        while m := pattern.match(n):
            nn += str(len(m[0])) + m[1]
            n = n.removeprefix(m[0])

        n = nn

    return len(n)


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {solve(inp, 1)}")
    print(f"Part 2: {solve(inp, 2)}")
