from euler import fibonacci


def main():
    f = fibonacci.fibonacci()
    n = next(f)
    s = 0
    while n < 4_000_000:
        if n % 2 == 0:
            s += n
        n = next(f)
    print(s)


if __name__ == "__main__":
    main()
