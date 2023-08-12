#!/usr/bin/python3

import sys


def sos():
    """def sos() -> None
This function convert the messages to Morse Code."""
    MORSE_CODE_DICT = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        else:
            input = sys.argv[1]
        ret = ""
        for c in input:
            if c.isalpha() or c == " ":
                ret += MORSE_CODE_DICT[c.upper()] + " "
            else:
                raise AssertionError("the arguments are bad")

        print(ret[:-1])

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    # print(sos.__doc__)
    sos()
