#!/usr/bin/python3

import sys


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """def give_bmi(height: list[int | float], weight: list[int | float])
-> list[int | float]

this function calculate bmi."""
    if type(height) is not list or type(weight) is not list:
        print("AssertionError: check input type.", file=sys.stderr)
        return

    if len(height) is not len(weight):
        print("AssertionError: check list length.", file=sys.stderr)
        return
    ret = []
    for h, w in zip(height, weight):
        if (type(h) is not int and type(h) is not float) or (
            type(w) is not int and type(w) is not float
        ):
            print("AssertionError: check list values.", file=sys.stderr)
            return
        ret.append(w / h**2)
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """def apply_limit(bmi: list[int | float], limit: int) -> list[bool]

return the list values of bool types.
True for above the limit."""
    if type(bmi) is not list or type(limit) is not int:
        print("AssertionError: check input type.", file=sys.stderr)
        return

    ret = []
    for b in bmi:
        if type(b) is not int and type(b) is not float:
            print("AssertionError: check list values.", file=sys.stderr)
            return
        ret.append(b > limit)
    return ret


def main() -> None:
    """print give_bmi and apply_limit docs."""

    print(give_bmi.__doc__)
    print(apply_limit.__doc__)


if __name__ == "__main__":
    main()
