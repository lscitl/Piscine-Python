#!/usr/bin/python3

import sys
from in_out import outer
from in_out import square
from in_out import pow


if __name__ == "__main__":
    try:
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
        print(type(my_counter))

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)
