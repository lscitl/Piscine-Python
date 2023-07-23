#!/usr/bin/python3

import sys
from S1E9 import Character, Stark


if __name__ == "__main__":
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

        hodor = Character("hodor")

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)
