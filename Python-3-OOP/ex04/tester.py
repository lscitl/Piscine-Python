#!/usr/bin/python3

import sys
from ft_calculator import calculator


if __name__ == '__main__':
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)

        # c = (1, 2, 3)
        # calculator.dotproduct(a, c)

    except Exception as e:
        print("Error:", e, file=sys.stderr)

    try:
        a = [5, 10, 'c']
        b = [2, 4, 3]
        calculator.dotproduct(a, b)

    except Exception as e:
        print("Error:", e, file=sys.stderr)
