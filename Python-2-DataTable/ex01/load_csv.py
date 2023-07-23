#!/usr/bin/python3

import sys
import pandas as pd
import os


def get_cur_dir() -> str:
    """
    def get_cur_dir() -> str:

    get absolute path of current directory.
    """

    abs_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(abs_path)
    return cur_dir


def load(path: str) -> pd.DataFrame:
    """
    def load(path: str) -> pd.DataFrame:

    load data to pandas dataset
    """

    cur_dir = get_cur_dir()
    if type(path) != str:
        raise AssertionError("invalid input type")
    new_path = cur_dir + '/' + path
    data = pd.read_csv(new_path, header=0)
    print("Loading dataset of dimensions:", data.shape)
    return data


def main():
    try:
        print(load("life_expectancy_years.csv"))

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
