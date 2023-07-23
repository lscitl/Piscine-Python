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

        new_data = pd.DataFrame({
            "gdp": inc_data.T.loc[year], "life": life_data.T.loc[year]
            }).dropna()
        new_data = new_data.reset_index()
        new_data.sort_values("country")

        new_data.plot.scatter(x="gdp", y="life", logx=True)

        # for i, country in enumerate(new_data["country"]):
        #     plt.scatter([], [], label=country)
        # plt.legend(new_data['country'], loc="lower right")

        xax = [300, 1000, 10000]
        plt.xticks(
            xax,
            [f"{val/1000:.0f}k" if val >= 1000 else str(val) for val in xax]
        )
        plt.title(year)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()

    except AssertionError as e:
        print("AssertionError:", e, file=sys.stderr)

    except Exception as e:
        print("Error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
    print(load.__doc__)
