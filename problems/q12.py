from functools import reduce
from operator import mul
import itertools

from euler import prime


def triangle_nums():
    n = 0
    counter = itertools.count(1)
    while True:
        n += next(counter)
        yield n


def main():
    t = triangle_nums()
    while True:
        n = next(t)
        facs = prime.prime_factors(n)
        combos = reduce(
            lambda acc, new: acc.union(set(new)),
            [list(itertools.combinations(facs, n)) for n in range(1, len(facs))],
            set(),
        )
        divisors = (
            reduce(
                lambda acc, _: acc + 1,
                filter(
                    lambda x: n % x == 0, [reduce(mul, combo, 1) for combo in combos]
                ),
                0,
            )
            + 2
        )

        if divisors > 500:
            print(n)
            print(divisors)
            break


if __name__ == "__main__":
    main()
