from typing import Iterator
from euler import restrictions


def fibonacci() -> Iterator[int]:
    q = [1, 1]
    yield 1
    yield 1
    i = 0
    while True:
        n = sum(q)
        yield n
        q[i] = n
        i += 1
        i %= 2


@restrictions.constrain_positive
def nth_fib(n: int) -> int:
    if n < 70:  # can probably go a little higher
        _phi = (1 + 5**0.5) / 2
        return int((_phi**n - (-_phi) ** -n) / (5**0.5))
    f = fibonacci()
    for _ in range(n - 1):
        next(f)
    return next(f)


@restrictions.constrain_positive_or_zero
def n_fibonacci(n) -> Iterator[int]:
    f = fibonacci()
    for i in range(n):
        yield next(f)
