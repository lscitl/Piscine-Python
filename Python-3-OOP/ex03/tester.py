#!/usr/bin/python3

import sys
from ft_calculator import calculator


if __name__ == '__main__':
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
        print('div 0 test')
        v3 / 0

        v4 = calculator((0.0, 1.0, 2.0))
        v4 + 1

    except Exception as e:
        print("Error:", e, file=sys.stderr)

    try:
        v4 = calculator([1, 2, 3, 'j'])
        v4 + 1

    except Exception as e:
        print("Error:", e, file=sys.stderr)
