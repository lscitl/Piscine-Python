#!/usr/bin/python3

class calculator:
    """calculator class. Only accept list type with numeric type elements."""
    def __init__(self, lst: list) -> None:
        """calculator class value initialize"""
        if type(lst) != list:
            raise AssertionError("only accept list type.")
        for i in lst:
            if type(i) != int and type(i) != float and type(i) != complex:
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
        """/ operator overloading of calculator class and prints results."""
        for i in range(len(self.lst)):
            self.lst[i] -= object
        print(self.lst)


if __name__ == "__main__":
    print(calculator.__doc__)
    print(calculator.__add__.__doc__)
