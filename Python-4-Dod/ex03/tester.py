#!/usr/bin/python3

import sys
from new_student import Student


if __name__ == "__main__":
    student = Student(name="Edward", surname="agle")
    print(student)

    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)

    except Exception as e:
        print('---------')
        print("Error:", e, file=sys.stderr)
        print('---------')

    student = Student(name="Edward", surname="agle", active=False)
    print(student)

    try:
        student = Student(name="Edward", surname="agle", asdf=False)
        print(student)

    except Exception as e:
        print('---------')
        print("Error:", e, file=sys.stderr)
        print('---------')

    try:
        student = Student(name="Edward")
        print(student)

    except Exception as e:
        print('---------')
        print("Error:", e, file=sys.stderr)
        print('---------')

    try:
        student = Student(name="Edward", surname='asdf', login='qwer')
        print(student)

    except Exception as e:
        print('---------')
        print("Error:", e, file=sys.stderr)
        print('---------')
