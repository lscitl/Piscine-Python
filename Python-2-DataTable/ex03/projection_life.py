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

        pop_data = load("population_total.csv")

        if pop_data.size == 0:
            raise AssertionError("No data")
        pop_data.set_index("country", inplace=True)
        pop_data.replace(
            {"k": "e+03", "M": "e+06", "B": "e+09"}, regex=True, inplace=True
        )
        pop_data[pop_data.columns] = (
            pop_data[pop_data.columns].astype(float).astype(int)
        )

        # pop_data = pop_data.loc[:, year]
        if pop_data.size == 0:
            raise AssertionError("There is no population data.")

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

        # print(pop_data)
        # print(inc_data)
        # print(pop_data.T.loc[year])

        new_data = pd.merge(pop_data.T.loc[year], inc_data.T.loc[year], how="inner", on='country')
        # new_data.pivot(index=new_data.index, columns=year + '_x', values=year + '_y')
        print(new_data)

        # if inc_data.size == 0:
        #     raise AssertionError("There is no income data.")

        # plt.legend(loc="lower right")

        # plt.title(year)
        # plt.xlabel("Gross domestic product")
        # plt.ylabel("Life Expectancy")

        # plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
