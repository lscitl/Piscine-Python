#!/usr/bin/python3

import sys
from in_out import outer
from in_out import square
from in_out import pow


if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
    print("---")
    print("type of my_counter:", type(my_counter))
    print("---")

    try:
        print(outer("3", square))
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    try:
        print(outer(3, 2))
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)
