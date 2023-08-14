#!/usr/bin/python3

import sys
from new_student import Student


if __name__ == "__main__":

    print('------------------------')
    student = Student(name="Edward", surname="agle")
    print(student)
    print('------------------------')
    student = Student(name="Edward", surname="agle", active=False)
    print(student)
    print('------------------------')

    try:
        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)
    print('------------------------')

    try:
        student = Student(name="Edward", surname="agle", asdf=False)
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)
    print('------------------------')

    try:
        student = Student(name="Edward")
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)

    print('------------------------')
    try:
        student = Student(name="Edward", surname='asdf', login='qwer')
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)
    print('------------------------')

    try:
        student = Student(name="", surname='asdf')
    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)
    print('------------------------')

    try:
        student = Student(name="a", surname='')
    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)
    print('------------------------')

    try:
        student = Student(name=123, surname='asdf')
    except TypeError as e:
        print("TypeError:", e, file=sys.stderr)
    print('------------------------')
