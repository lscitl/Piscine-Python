#!/usr/bin/python3

"""
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

import sys
import string
import collections
from typing import Any, Callable, Generic, Iterable, TypeVar, overload

from typing_extensions import Self, TypeGuard


_T = TypeVar("_T")
_S = TypeVar("_S")
_T_co = TypeVar("_T_co", covariant=True)


Iterator = collections.abc.Iterator


class ft_filter(Iterator[_T], Generic[_T]):
    @overload
    def __init__(self, __function: None,
                 __iterable: Iterable[_T]) -> None: ...

    @overload
    def __init__(self, __function: None,
                 __iterable: Iterable[None]) -> None: ...

    @overload
    def __init__(self, __function: Callable[[
                 _S], TypeGuard[_T]], __iterable: Iterable[_S]) -> None: ...

    @overload
    def __init__(self, __function: Callable[[
                 _T], Any], __iterable: Iterable[_T]) -> None: ...

    def __iter__(self) -> Self: ...
    def __next__(self) -> _T: ...


def main():
    try:
        punc = string.punctuation
        ret = [0, 0, 0, 0, 0]
        if len(sys.argv) == 1:
            print("What is the text to count?")
            input = sys.stdin.readline()
        elif len(sys.argv) == 2:
            input = sys.argv[1]
        else:
            raise AssertionError("Too many args")
        for c in input:
            if c.isalpha():
                if c == c.capitalize():
                    ret[0] += 1
                else:
                    ret[1] += 1
            elif c in punc:
                ret[2] += 1
            elif c.isspace():
                ret[3] += 1
            elif c.isdigit():
                ret[-1] += 1
        print("The text contains {strlen} characters:".format(
            strlen=len(input)))
        print("{upper} upper letters".format(upper=ret[0]))
        print("{lower} lower letters".format(lower=ret[1]))
        print("{punctuation} punctuation mark".format(punctuation=ret[2]))
        print("{spaces} spaces".format(spaces=ret[3]))
        print("{digits} digits".format(digits=ret[-1]))
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    # print(__doc__)
    main()
