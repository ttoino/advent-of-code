if __name__ == "__main__":
    a = input().strip().split()
    row, column = int(a[-3].removesuffix(",")), int(a[-1].removesuffix("."))

    x = row - 2 + column
    n = x * (x + 1) // 2 + column

    r = 20151125
    i = 1
    while i < n:
        i += 1
        r *= 252533
        r %= 33554393

    print(f"Solution: {r}")
