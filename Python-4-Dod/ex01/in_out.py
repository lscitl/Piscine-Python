#!/usr/bin/python3

def square(x: int | float) -> int | float:
    """return square value."""
    if not isinstance(x, (int, float)):
        raise TypeError("invalid input type.")
    return x ** 2


def pow(x: int | float) -> int | float:
    """return pow value.(x ** x)"""
    if not isinstance(x, (int, float)):
        raise TypeError("invalid input type.")
    return x ** x


def outer(x: int | float, function) -> object:
    """outer fuction which takes value with function."""

    if not isinstance(x, (int, float)) or not callable(function):
        raise TypeError("invalid input type.")

    count = 0

    def inner() -> int | float:
        """inner function of outer function."""
        nonlocal x, count
        count += 1
        # print("function called:", count)
        x = function(x)
        return x
    return inner


if __name__ == "__main__":
    print(outer.__doc__)
