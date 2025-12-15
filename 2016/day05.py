import itertools as it
from hashlib import md5


def part1(id: str) -> str:
    result = ""

    for i in it.count():
        if (h := md5(bytes(f"{id}{i}", encoding="ascii")).hexdigest()).startswith(
            "00000"
        ):
            result += h[5]

            if len(result) == 8:
                break

    return result


def part2(id: str) -> str:
    password = ["_"] * 8

    for i in it.count():
        if (h := md5(bytes(f"{id}{i}", encoding="ascii")).hexdigest()).startswith(
            "00000"
        ):
            pos = h[5]
            if pos.isdigit() and (pos := int(pos)) < 8 and password[pos] == "_":
                password[pos] = h[6]
                if "_" not in password:
                    break

    return "".join(password)


if __name__ == "__main__":
    id = input()

    print(f"Part 1: {part1(id)}")
    print(f"Part 2: {part2(id)}")
