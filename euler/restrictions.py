from typing import Any


def _constrain_int(n: Any) -> None:
    if not isinstance(n, int):
        raise ValueError("%s is not an integer" % type(n))


def _constrain_positive_int(n: Any, allow_zero: bool = False) -> None:
    _constrain_int(n)
    if n < int(not allow_zero):
        raise ValueError("%s is not positive%s" % (n, " or zero" if allow_zero else ""))


def constrain_positive(f):
    def wrapper(n, **kwargs):
        _constrain_positive_int(n)
        return f(n, **kwargs)

    return wrapper


def constrain_positive_or_zero(f):
    def wrapper(n, **kwargs):
        _constrain_positive_int(n, allow_zero=True)
        return f(n, **kwargs)

    return wrapper
