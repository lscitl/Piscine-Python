#!/usr/bin/python3

import sys


class calculator:
    """calculator class. Only accept list type with numeric type elements."""
    def __init__(self, lst: list) -> None:
        """calculator class value initialize"""
        if not isinstance(lst, list):
            raise AssertionError("only accept list type.")
        for i in lst:
            if not self._is_numeric(i):
                raise AssertionError(
                    "list element can not apply arithmetic operator."
                )
        self.lst = lst

    def __add__(self, object) -> None:
        """+ operator overloading of calculator class and prints results."""
        for i in range(len(self.lst)):
            self.lst[i] += object
        print(self.lst)

    def __mul__(self, object) -> None:
        """* operator overloading of calculator class and prints results."""
        for i in range(len(self.lst)):
            self.lst[i] *= object
        print(self.lst)

    def __sub__(self, object) -> None:
        """- operator overloading of calculator class and prints results."""
        for i in range(len(self.lst)):
            self.lst[i] -= object
        print(self.lst)

    def __truediv__(self, object) -> None:
        """/ operator overloading of calculator class and prints results.
Divide by zero will print error msg and return None."""
        try:
            for i in range(len(self.lst)):
                self.lst[i] /= object
            print(self.lst)

        except Exception as e:
            print("Error:", e, file=sys.stderr)

    def _is_numeric(self, object) -> bool:
        return isinstance(object, (int, float, complex))


if __name__ == "__main__":
    print(calculator.__doc__)
    print(calculator.__add__.__doc__)
