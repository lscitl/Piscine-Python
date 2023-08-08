#!/usr/bin/python3

import sys


def slice_me(family: list, start: int, end: int) -> list:
    """def slice_me(family: list, start: int, end: int) -> list
Check input list is 2D array, and slice it."""

    if type(
        family
    ) is not list or type(start) is not int or type(end) is not int:
        print("AssertionError: input type error", file=sys.stderr)
        return family

    column = len(family)
    if column == 0:
        print("AssertionError: input type error", file=sys.stderr)
        return family

    if type(family[0]) is not list:
        print("AssertionError: input type error", file=sys.stderr)
        return family

    row = len(family[0])
    if row == 0:
        print("AssertionError: input value error", file=sys.stderr)
        return family

    if (start >= column or start < -column) or (
        end >= column or end < -column
    ):
        print("AssertionError: index range error", file=sys.stderr)
        return family

    for c in family:
        if len(c) != row:
            print("AssertionError: list length error", file=sys.stderr)
            return family

    print(f"My shape is : ({column}, {row})")
    ret = family[start:end]
    print(f"My new shape is : ({len(ret)}, {row})")
    return ret


if __name__ == "__main__":
    print(slice_me.__doc__)
