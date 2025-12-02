import itertools as it
from hashlib import md5


def solve(inp: str, prefix: str):
    for i in it.count():
        if md5(bytes(f"{inp}{i}", encoding="ascii")).hexdigest().startswith(prefix):
            return i


if __name__ == "__main__":
    inp = input().strip()

    print(f"Part 1: {solve(inp, '00000')}")
    print(f"Part 2: {solve(inp, '000000')}")
