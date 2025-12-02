def solve(t: int, part: int):
    houses = list(0 for _ in range(t + 1))

    for i in range(1, t + 1):
        for j in range(i, t + 1 if part == 1 else min(t + 1, i * 50 + 1), i):
            houses[j] += i

    return next(i for i, x in enumerate(houses) if x >= (t if part == 1 else t * 10))


if __name__ == "__main__":
    t = int(input().strip()) // 10
