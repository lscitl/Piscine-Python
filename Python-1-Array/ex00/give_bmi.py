#!/usr/bin/python3

import sys


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    def give_bmi(height: list[int | float], weight: list[int | float])
    -> list[int | float]

    this function calculate bmi.
    """
    if type(height) != list or type(weight) != list:
        print("AssertionError: check input type.", file=sys.stderr)
        return

    if len(height) != len(weight):
        print("AssertionError: check list length.", file=sys.stderr)
        return
    ret = []
    for h, w in zip(height, weight):
        if (type(h) != int and type(h) != float) or (
            type(w) != int and type(w) != float
        ):
            print("AssertionError: check list values.", file=sys.stderr)
            return
        ret.append(w / h**2)
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    def apply_limit(bmi: list[int | float], limit: int) -> list[bool]

    return the list values of bool types.
    True for above the limit.
    """
    if type(bmi) != list or type(limit) != int:
        print("AssertionError: check input type.", file=sys.stderr)
        return

    ret = []
    for b in bmi:
        if type(b) != int and type(b) != float:
            print("AssertionError: check list values.", file=sys.stderr)
            return
        ret.append(b > limit)
    return ret


def main() -> None:
    """
    print give_bmi and apply_limit docs.
    """

    print(give_bmi.__doc__)
    print(apply_limit.__doc__)


if __name__ == "__main__":
    main()
