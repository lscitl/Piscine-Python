#!/usr/bin/python3


import sys
import string


def building():
    """building function works with 0 or 1 arg.
If arg 0, it will take standard input."""
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
    # print(building.__doc__)
    building()
