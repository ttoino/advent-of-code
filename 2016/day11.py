import itertools as it
import heapq as hq


def is_valid(state: tuple[int, ...], size: int):
    if 0 in state or 5 in state:
        return False

    for i in range(0, size, 2):
        if not state[i] == state[i + 1] and any(
            state[j] == state[i] for j in range(1, size, 2)
        ):
            return False

    return True


def tuple_helper(state: tuple[int, ...], i: int, d: int):
    new_state = list(state)
    new_state[i] += d
    return tuple(new_state)


def h(state: tuple[int, ...]):
    return sum(4 - i for i in state)


def next_states(state: tuple[int, ...], size: int):
    current_level = state[size]
    in_current_level = [i for i, v in enumerate(state[:-1]) if v == current_level]

    for d in -1, 1:
        st = tuple_helper(state, size, d)

        for i in in_current_level:
            s = tuple_helper(st, i, d)
            if is_valid(s, size):
                yield s

        for i, j in it.combinations(in_current_level, 2):
            s = tuple_helper(tuple_helper(st, i, d), j, d)
            if is_valid(s, size):
                yield s


def solve(part2: bool) -> int:
    size = 14 if part2 else 10
    target = (4,) * (size + 1)
    start = (
        (1, 1, 1, 1, 1, 1, 3, 2, 3, 2, 3, 2, 3, 2, 1)
        if part2
        else (1, 1, 3, 2, 3, 2, 3, 2, 3, 2, 1)
    )

    visited = set()
    heap = [(0, 0, start)]

    while len(heap) > 0:
        s, d, state = hq.heappop(heap)

        if state in visited:
            continue

        visited.add(state)

        if state == target:
            return d

        for s in next_states(state, size):
            hq.heappush(heap, (d + 1 + h(state), d + 1, s))

    return -1


if __name__ == "__main__":
    print(f"Part 1: {solve(False)}")
    print(f"Part 2: {solve(True)}")
