#!/usr/bin/python3

def square(x: int | float) -> int | float:
    """return square value."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """return pow value.(x ** x)"""
    return x ** x


def outer(x: int | float, function) -> object:
    """outer fuction which takes value with function."""
    count = x

    def inner() -> float:
        """inner function of outer function."""
        nonlocal count
        count = function(count)
        return count
    return inner


if __name__ == "__main__":
    print(outer.__doc__)
