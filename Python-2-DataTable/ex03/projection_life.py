#!/usr/bin/python3

import sys
from load_csv import load, pd
import matplotlib.pyplot as plt


def main():
    """
    Population Projections Plot of South Korea vs France.
    """

    try:
        year = str(1900)

        life_data = load("life_expectancy_years.csv")

        if life_data.size == 0:
            raise AssertionError("No data")
        life_data.set_index("country", inplace=True)

        inc_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )

        if inc_data.size == 0:
            raise AssertionError("No data")
        inc_data.set_index("country", inplace=True)
        inc_data.replace(
            {"k": "e+03", "M": "e+06", "B": "e+09"}, regex=True, inplace=True
        )
        inc_data[inc_data.columns] = (
            inc_data[inc_data.columns].astype(float).astype(int)
        )

        if inc_data.size == 0:
            raise AssertionError("There is no income data.")

        new_data = pd.merge(inc_data.T.loc[year], life_data.T.loc[year], how="inner", on='country')
        new_data.plot.scatter(x=year + '_x', y=year + '_y')

        # plt.legend(loc="lower right")
        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale('log')

        plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
