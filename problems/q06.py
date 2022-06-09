from functools import reduce


def main():
    print(sum(range(101)) ** 2 - reduce(lambda a, b: a + b**2, range(1, 101), 0))


if __name__ == "__main__":
    main()
