#!/usr/bin/python3


from typing import Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar("T")


class ft_filter(Iterator[T], Generic[T]):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    @overload
    def __init__(self, __function: None, __iterable: Iterable[T]) -> None:
        ...

    @overload
    def __init__(
        self, __function: Callable[[T], bool], __iterable: Iterable[T]
    ) -> None:
        ...

    def __init__(self, __function, __iterable) -> None:
        '''initialize ft_filter'''
        self.func = __function
        self.filtered_list = [
            v for v in __iterable if self.func is None or self.func(v)
        ]
        self.idx = 0

    def __iter__(self) -> 'ft_filter[T]':
        '''set iterator'''
        return self

    def __next__(self) -> T:
        '''set next function'''
        if self.idx >= len(self.filtered_list):
            raise StopIteration
        val = self.filtered_list[self.idx]
        self.idx += 1
        return val


if __name__ == "__main__":
    # print(filter.__doc__)
    # print(ft_filter.__doc__)

    og = filter.__doc__
    ft = ft_filter.__doc__

    print(og == ft)
