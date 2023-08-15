#!/usr/bin/python3

import sys
from callLimit import callLimit


if __name__ == "__main__":
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()

    try:
        @callLimit("a")
        def f():
            print("f()")
    except Exception as e:
        print("Error:", e, file=sys.stderr)

    try:
        @callLimit(-1)
        def f():
            print("f()")
    except Exception as e:
        print("Error:", e, file=sys.stderr)
