#!/usr/bin/python3

import sys


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """def give_bmi(height: list[int | float], weight: list[int | float])
-> list[int | float]

this function calculate bmi."""

    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("check input type.")

        if len(height) is not len(weight):
            raise AssertionError("check list length.")

        ret = []
        for h, w in zip(height, weight):
            if isinstance(h, (int, float)) or isinstance(w, (int, float)):
                raise ValueError("check list values.")
            ret.append(w / (h ** 2))
        return ret

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """def apply_limit(bmi: list[int | float], limit: int) -> list[bool]

return the list values of bool types.
True for above the limit."""

    try:
        if not isinstance(bmi, list) or not isinstance(limit, int):
            raise TypeError("check input type.")

        ret = []
        for b in bmi:
            if not isinstance(b, (int, float)):
                raise AssertionError("check input type.")
            ret.append(b > limit)
        return ret

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def main() -> None:
    """print give_bmi and apply_limit docs."""

    print(give_bmi.__doc__)
    print(apply_limit.__doc__)


if __name__ == "__main__":
    main()
