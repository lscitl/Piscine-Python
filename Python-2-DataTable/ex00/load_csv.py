#!/usr/bin/python3

import sys
import pandas as pd
import os


def get_cur_dir() -> str:
    """def get_cur_dir() -> str:

get absolute path of current directory."""

    abs_path = os.path.abspath(__file__)
    cur_dir = os.path.dirname(abs_path)
    return cur_dir


def load(path: str) -> pd.DataFrame:
    """def load(path: str) -> pd.DataFrame:

load data to pandas dataset"""

    if not isinstance(path, str):
        raise AssertionError("invalid input type")

    if not path:
        raise ValueError("invalid input value")

    # unix abs path
    if not os.path.isabs(path):
        path = get_cur_dir() + '/' + path

    data = pd.read_csv(path, header=0)
    print("Loading dataset of dimensions:", data.shape)

    return data


def main():
    """testing load function."""
    try:
        print(load("life_expectancy_years.csv"))

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except ValueError as e:
        print("ValueError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)