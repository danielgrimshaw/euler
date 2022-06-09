from typing import List, Iterator

import itertools

from euler import restrictions


@restrictions.constrain_positive
def prime_factors(n: int) -> List[int]:
    if n == 1:
        return [n]
    p = generate_primes()
    i = next(p)
    working = n
    facs = []
    while i <= working**0.5:
        if working % i == 0:
            working /= i
            facs.append(i)
        else:
            i = next(p)
    return facs + [int(working)]


def generate_primes() -> Iterator[int]:
    # Hard code some primes to get the generator going
    yield 2
    yield 3
    yield 5
    yield 7

    sieve = {}
    prime_generator = generate_primes()

    p = next(prime_generator) and next(prime_generator)
    q = p * p
    for c in itertools.count(9, 2):
        if c in sieve:
            s = sieve.pop(c)
        elif c < q:
            yield c  # c must be prime
            continue
        else:  # c == q
            s = itertools.count(q + 2 * p, 2 * p)
            p = next(prime_generator)
            q = p * p
        for multiple in s:
            if multiple not in sieve:  # no duplicates
                sieve[multiple] = s
                break


@restrictions.constrain_positive
def n_primes(n: int) -> Iterator[int]:
    i = 0
    p = generate_primes()
    while i < n:
        yield next(p)
        i += 1


@restrictions.constrain_positive_or_zero
def nth_prime(n: int) -> int:
    p = generate_primes()
    for i in range(n - 1):
        next(p)
    return next(p)
