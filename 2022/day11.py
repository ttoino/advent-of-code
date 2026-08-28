import sys

import functools as ft
import operator as op
from collections import deque



monkeys = []
divisor = 0


class Monkey:
    __slots__ = ('items', 'operation', 'test', 'true_monkey', 'false_monkey', 'inspections')

    def __init__(self, i: deque[int], op: str, d: int, t: int, f: int):
        self.items = i
        self.operation = op
        self.test = d
        self.true_monkey = t
        self.false_monkey = f
        self.inspections = 0

    def inspect(self):
        self.inspections += len(self.items)
        while len(self.items):
            old = self.items.popleft()
            i = eval(self.operation)
            i //= 3
            if i % self.test == 0:
                monkeys[self.true_monkey].items.append(i)
            else:
                monkeys[self.false_monkey].items.append(i)


class Monkey_p2:
    __slots__ = ('items', 'operation', 'test', 'true_monkey', 'false_monkey', 'inspections')

    def __init__(self, i: deque[int], op: str, d: int, t: int, f: int):
        self.items = i
        self.operation = op
        self.test = d
        self.true_monkey = t
        self.false_monkey = f
        self.inspections = 0

    def inspect(self):
        self.inspections += len(self.items)
        for _ in range(len(self.items)):
            old = self.items.popleft()
            i = eval(self.operation)
            i %= divisor
            if i % self.test == 0:
                monkeys[self.true_monkey].items.append(i)
            else:
                monkeys[self.false_monkey].items.append(i)


def parse(s: str) -> list[tuple[list[int], str, int, int, int]]:
    res = []
    for block in s.strip().split('\n\n'):
        lines = block.splitlines()
        i = [int(i) for i in lines[1].split(': ')[1].split(', ')]
        op = lines[2].split('= ')[1]
        d = int(lines[3].split('by ')[1])
        t = int(lines[4][-1])
        f = int(lines[5][-1])
        res.append((i, op, d, t, f))
    return res


def part1(inp: list[tuple[list[int], str, int, int, int]]):
    global monkeys
    monkeys = [Monkey(deque(m[0]), *m[1:]) for m in inp]
    for _ in range(20):
        for m in monkeys:
            m.inspect()
    monkeys.sort(key=lambda x: x.inspections)
    return monkeys[-1].inspections * monkeys[-2].inspections


def part2(inp: list[tuple[list[int], str, int, int, int]]):
    global monkeys, divisor
    monkeys = [Monkey_p2(deque(m[0]), *m[1:]) for m in inp]
    divisor = ft.reduce(op.mul, map(lambda x: x.test, monkeys), 1)
    for _ in range(10000):
        for m in monkeys:
            m.inspect()
    monkeys.sort(key=lambda x: x.inspections)
    return monkeys[-1].inspections * monkeys[-2].inspections


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
