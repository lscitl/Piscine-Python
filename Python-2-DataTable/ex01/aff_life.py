#!/usr/bin/python3

import sys
from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Life expectancy Projections Plot of South Korea."""

    try:
        data = load("life_expectancy_years.csv")

        if data.size == 0:
            raise AssertionError("No data")

        kr_data = data.set_index("country").loc['South Korea']

        if kr_data.size == 0:
            raise AssertionError("There is no South Korea data.")

        kr_data.plot(kind="line")

        # fr_data = data.set_index("country").loc['France']
        # fr_data.plot(kind="line")

        plt.title('South Korea Life expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life expectancy')
        plt.legend(loc='lower right')

        plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
