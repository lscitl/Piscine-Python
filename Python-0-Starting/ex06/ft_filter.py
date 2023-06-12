#!/usr/bin/python3

"""
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

from typing import Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar("T")


# class ft_filter:
class ft_filter(Iterator[T], Generic[T]):
    @overload
    def __init__(self, __function: None, __iterable: Iterable[T]) -> None:
        ...

    @overload
    def __init__(
        self, __function: Callable[[T], bool], __iterable: Iterable[T]
    ) -> None:
        ...

    def __init__(self, __function, __iterable) -> None:
        self.func = __function
        self.iterable = __iterable
        self.iterator = iter(__iterable)

    # def __iter__(self):
    #     return self

    # def __list__(self):
    #     return [val for val in self]

    def __iter__(self):
        return (
            val for val in self.iterable if self.func is None or self.func(val)
        )

    def __next__(self):
        while True:
            value = next(self.iterator)
            if self.func is None or self.func(value):
                return value


if __name__ == "__main__":
    print(__doc__)
