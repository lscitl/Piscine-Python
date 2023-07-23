#!/usr/bin/python3

import sys
from S1E7 import Baratheon, Lannister


if __name__ == "__main__":
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(
            f"Name : {Jaine.first_name, type(Jaine).__name__}" +
            f", Alive : {Jaine.is_alive}"
        )

        print(str(Robert))
        print(repr(Robert))

    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)
