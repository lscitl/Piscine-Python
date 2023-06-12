#!/usr/bin/python3

import sys


def whatis(args):
    if len(args) > 2:
        raise AssertionError("more than one argument are provided")
    elif len(args) == 2:
        try:
            arg = float(args[1])
            if arg == int(arg):
                if arg % 2 == 1:
                    print("I'm Odd.")
                else:
                    print("I'm Even.")
            else:
                raise AssertionError("argument is not an integer")
        except ValueError:
            raise AssertionError("argument is not an integer")


if __name__ == "__main__":
    try:
        whatis(sys.argv)
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
