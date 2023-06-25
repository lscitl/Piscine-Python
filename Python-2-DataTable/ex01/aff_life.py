#!/usr/bin/python3

import sys
from load_csv import load
import matplotlib.pyplot as plt


def main():

    data = load("../life_expectancy_years.csv")

    try:
        if data.size == 0:
            raise AssertionError("No data")
        print(data)
        data.plot(kind="line", y='value')

        plt.title('Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')

        plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
