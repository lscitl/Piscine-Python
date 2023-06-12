#!/usr/bin/python3

"""
filterstring
"""

import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        else:
            input = sys.argv[1].split()
            n = int(sys.argv[2])
        print([word for word in ft_filter(lambda x: len(x) > n, input)])

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
