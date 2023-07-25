#!/usr/bin/python3

import sys
from callLimit import callLimit


if __name__ == "__main__":
    try:
        @callLimit(3)
        def f():
            print("f()")

        @callLimit(1)
        def g():
            print("g()")

        for i in range(3):
            f()
            g()

    except Exception as e:
        print("Error:", e, file=sys.stderr)
