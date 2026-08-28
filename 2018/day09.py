import itertools as it
import sys
from typing import Self


class CircularList:
    def __init__(self):
        self.current = None

    def insert(self, value):
        if self.current == None:
            self.current = self.Node(value)
        else:
            next = self.current.next
            new_node = self.Node(value, self.current, next)
            self.current.next = new_node
            next.prev = new_node
            self.current = new_node

    def pop(self):
        current = self.current
        self.current = current.next
        current.prev.next = self.current
        return current.value

    def skip_clockwise(self, n: int):
        for _ in range(n):
            self.current = self.current.next

    def skip_counterclockwise(self, n: int):
        for _ in range(n):
            self.current = self.current.prev

    class Node:
        def __init__(self, value, prev: Self = None, next: Self = None):
            self.value = value
            self.prev = prev or self
            self.next = next or self


def part1(inp: tuple[int, int]):
    player_count, max_n = inp
    circle = [0]
    current = 0
    players = [0 for _ in range(player_count)]
    for n, player in zip(range(1, max_n + 1), it.cycle(range(player_count))):
        if n % 23 == 0:
            current -= 7
            current %= len(circle)
            players[player] += n + circle.pop(current)
            continue
        current += 2
        current %= len(circle)
        circle.insert(current, n)
    return max(players)


def part2(inp: tuple[int, int]):
    player_count, max_n = inp
    max_n *= 100
    circle = CircularList()
    circle.insert(0)
    players = [0 for _ in range(player_count)]
    for n, player in zip(range(1, max_n + 1), it.cycle(range(player_count))):
        if n % 23 == 0:
            circle.skip_counterclockwise(7)
            players[player] += n + circle.pop()
            continue
        circle.skip_clockwise(1)
        circle.insert(n)
    return max(players)


if __name__ == "__main__":
    l = sys.stdin.read().strip().split()
    inp = (int(l[0]), int(l[6]))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
