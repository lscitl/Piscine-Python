#!/usr/bin/python3

import sys
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """def slice_me(family: list, start: int, end: int) -> list
Check input list is 2D array, and slice it."""

    try:
        if (
            not isinstance(family, list) or
            not isinstance(start, int) or
            not isinstance(end, int) or
            not all(map(lambda x: isinstance(x, list), family))
        ):
            raise TypeError("input type error.")

        tmp_array = np.array(family)

        if tmp_array.ndim != 2:
            raise AssertionError("input shape is not valid.")

        sliced_array = tmp_array[start: end]
        # no column case.
        if sliced_array.shape[0] == 0:
            raise AssertionError("slicing failure.")

        print(f"My shape is : {tmp_array.shape}")
        print(f"My new shape is : {sliced_array.shape}")
        return sliced_array.tolist()

    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)

    return family


if __name__ == "__main__":
    print(slice_me.__doc__)
