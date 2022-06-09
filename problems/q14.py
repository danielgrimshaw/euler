from functools import lru_cache


@lru_cache
def collatz(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + collatz(n // 2)
    return 1 + collatz(3 * n + 1)


def main():
    best = 0
    n = -1
    for i in range(1, 1_000_000):
        if collatz(i) > best:
            best = collatz(i)
            n = i
    print(n)


if __name__ == "__main__":
    main()
