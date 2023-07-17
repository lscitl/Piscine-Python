#!/usr/bin/python3

import sys
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    def load(path: str) -> pd.DataFrame:

    load data to pandas dataset
    """

    try:
        if type(path) != str:
            raise AssertionError("invalid input type")
        data = pd.read_csv(path)
        print("Loading dataset of dimensions:", data.shape)
        return data
    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


def main():
    print(load("population_total.csv"))


if __name__ == "__main__":
    main()
    print(load.__doc__)
