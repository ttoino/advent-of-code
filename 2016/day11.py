import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
import heapq as hq


def is_valid(state):
    if 0 in state or 5 in state:
        return False

    for i in range(0, 10, 2):
        if not state[i] == state[i + 1] and any(
                state[j] == state[i] for j in range(1, 10, 2)):
            return False
    return True


def tuple_helper(state, i, d):
    state = list(state)
    state[i] += d
    return tuple(state)


def h(state):
    return sum(4 - i for i in state)


def next_states(state):
    current_level = state[10]
    in_current_level = [
        i for i, v in enumerate(state[:-1]) if v == current_level
    ]

    for d in -1, 1:
        st = tuple_helper(state, 10, d)

        for i in in_current_level:
            s = tuple_helper(st, i, d)
            if is_valid(s):
                yield s

        for i, j in it.combinations(in_current_level, 2):
            s = tuple_helper(tuple_helper(st, i, d), j, d)
            if is_valid(s):
                yield s


with open("input") as inf, open("part1.out", "w+") as outf:
    target = (4,) * 11
    start = (1, 1, 3, 2, 3, 2, 3, 2, 3, 2, 1)

    visited = set()
    heap = [(0, 0, start)]

    while len(heap) > 0:
        s, d, state = hq.heappop(heap)

        if state in visited:
            continue

        visited.add(state)

        if state == target:
            outf.write(str(d))
            exit()

        for s in next_states(state):
            hq.heappush(heap, (d + 1 + h(state), d + 1, s))
