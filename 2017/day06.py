import itertools as it
import sys


def part1(inp: tuple[int, ...]) -> int:
    state = inp
    states = set()
    for step in it.count():
        if state in states:
            return step
            break
        states.add(state)
        i, n = max(enumerate(state), key=lambda x: (x[1], -x[0]))
        state = list(state)
        state[i] = 0
        for j in range(1, n + 1):
            state[(i + j) % len(state)] += 1
        state = tuple(state)


def part2(inp: tuple[int, ...]) -> int:
    state = inp
    states = {}
    for step in it.count():
        if state in states:
            return step - states[state]
            break
        states[state] = step
        i, n = max(enumerate(state), key=lambda x: (x[1], -x[0]))
        state = list(state)
        state[i] = 0
        for j in range(1, n + 1):
            state[(i + j) % len(state)] += 1
        state = tuple(state)


if __name__ == "__main__":
    inp = tuple(map(int, input().split()))

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
