#!/usr/bin/python3

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
