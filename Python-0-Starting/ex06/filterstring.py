#!/usr/bin/python3


import sys
from ft_filter import ft_filter


def filterstring() -> None:
    """filterstring function works with 2 args.
If second arg is not int, it will raise an error."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        input = sys.argv[1].split()
        if sys.argv[2].isdigit() is False:
            raise AssertionError(
                "second argument is not an integer."
            )
        n = int(sys.argv[2])

        filtered_ft = ft_filter(lambda x: len(x) > n, input)
        # print(iter(filtered_ft))
        print([word for word in filtered_ft])
        # print([word for word in filtered_ft])

        # filtered_og = filter(lambda x: len(x) > n, input)
        # print(iter(filtered_og))
        # print([word for word in filtered_og])
        # print([word for word in filtered_og])

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    # print(filterstring.__doc__)
    filterstring()
