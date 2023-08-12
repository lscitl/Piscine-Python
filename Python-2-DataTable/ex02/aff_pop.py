#!/usr/bin/python3

import sys
from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Population Projections Plot of South Korea vs France."""

    try:
        data = load("population_total.csv")

        if data.size == 0:
            raise AssertionError("No data")

        data.set_index('country', inplace=True)
        data.replace(
            {"k": "e+03", "M": "e+06", "B": "e+09"}, regex=True, inplace=True
        )
        data[data.columns] = data[data.columns].astype(float).astype(int)

        def formatter(x, pos):
            return str(int(round(x / 1e6, 1))) + 'M'

        year_begin = str(1800)
        year_end = str(2050)

        kr_data = data.loc['South Korea'][year_begin: year_end]
        # print(kr_data)
        if kr_data.size == 0:
            raise AssertionError("There is no South Korea data.")

        fr_data = data.loc['France'][year_begin: year_end]

        if fr_data.size == 0:
            raise AssertionError("There is no France data.")

        kr_data.plot(kind="line").yaxis.set_major_formatter(formatter)
        fr_data.plot(kind="line")

        plt.legend(loc='lower right')

        plt.title('Population Projections')
        plt.xlabel('Year')
        plt.ylabel('Population')

        plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)
    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
