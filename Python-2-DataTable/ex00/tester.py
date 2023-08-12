#!/usr/bin/python3

from load_csv import load
import sys

print(load("life_expectancy_years.csv"))

try:
    print(load("asdf"))

except AssertionError as e:
    print("AssertionError:", e, file=sys.stderr)

except Exception as e:
    print("Error:", e, file=sys.stderr)
