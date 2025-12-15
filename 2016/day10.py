import sys


class Robot:
    number: str
    give_low_to: str
    give_high_to: str
    v1: int
    v2: int
    part2: bool

    def __init__(self, n: str, part2: bool):
        self.number = n
        self.part2 = part2

    def ready(self):
        return (
            self.give_high_to is not None
            and self.give_low_to is not None
            and self.v1 is not None
            and self.v2 is not None
        )

    def handle(self):
        if not self.part2 and (
            (self.v1, self.v2) == (61, 17) or (self.v1, self.v2) == (17, 61)
        ):
            outputs["o0"] = int(self.number)

        if self.part2 and self.give_low_to.startswith("o"):
            outputs[self.give_low_to] = min(self.v1, self.v2)
        else:
            robots.setdefault(self.give_low_to, Robot(self.give_low_to, self.part2))
            robots[self.give_low_to].give_value(min(self.v1, self.v2))

        if self.part2 and self.give_high_to.startswith("o"):
            outputs[self.give_high_to] = max(self.v1, self.v2)
        else:
            robots.setdefault(self.give_high_to, Robot(self.give_high_to, self.part2))
            robots[self.give_high_to].give_value(max(self.v1, self.v2))

    def give_value(self, v: int):
        if self.v1 is None:
            self.v1 = v
        else:
            self.v2 = v

        if self.ready():
            self.handle()

    def set_low(self, r: str):
        self.give_low_to = r

        if self.ready():
            self.handle()

    def set_high(self, r: str):
        self.give_high_to = r

        if self.ready():
            self.handle()


robots: dict[str, Robot] = {}
outputs = {
    "o0": 1,
    "o1": 1,
    "o2": 1,
}


def solve(inp: list[list[str]], part2: bool) -> int:
    for i in inp:
        match i:
            case ["value", x, "goes", "to", "bot", y]:
                robots.setdefault(y, Robot(y, part2))
                robots[y].give_value(int(x))
            case ["bot", x, "gives", "low", "to", obl, y, "and", "high", "to", obh, z]:
                robots.setdefault(x, Robot(x, part2))
                robots[x].set_low(("" if obl == "bot" else "o") + y)
                robots[x].set_high(("" if obh == "bot" else "o") + z)

    return outputs["o0"] * outputs["o1"] * outputs["o2"]


if __name__ == "__main__":
    inp = [i.split() for i in sys.stdin.readlines()]

    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
