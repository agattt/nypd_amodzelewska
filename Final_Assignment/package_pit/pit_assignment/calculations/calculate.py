import pandas as pd


def taxed_income(data_frame, year, share, tax_threshold):

    data_frame["Podatek od osoby dla JST"] = \
        data_frame["Dochód z PIT w " + year] / (data_frame["Liczba ludności pracującej"])

    data_frame["Całkowity podatek zapłacony przez osobę"] = \
        data_frame["Podatek od osoby dla JST"]/share

    data_frame["Średni roczny dochód opodatkowany na osobę"] = \
        data_frame["Całkowity podatek zapłacony przez osobę"]/tax_threshold

    data_frame["Średni miesięczny dochód opodatkowany na osobę"] = \
        data_frame["Średni roczny dochód opodatkowany na osobę"]/12

    return data_frame


def variance(data_frame1, data_frame2, year):

    df_var = pd.DataFrame(
        columns=["Kod Jednostki Terytorialnej",
                 "Wariancja średniego rocznego dochodu w podległych JST",
                 "Wariancja średniego miesięcznego dochodu w podległych JST"]
        )

    df_var["Kod Jednostki Terytorialnej"] = data_frame1["Kod Jednostki Terytorialnej"]

    for i in range(len(df_var)):

        df_var.iloc[i, 1] = \
            data_frame2[data_frame2["Kod Jednostki Terytorialnej"].str[:len(df_var.iloc[i, 0])]
                        == df_var.iloc[i, 0]]["Średni roczny dochód opodatkowany na osobę"].var()

        df_var.iloc[i, 2] = \
            data_frame2[data_frame2["Kod Jednostki Terytorialnej"].str[:len(df_var.iloc[i, 0])]
                        == df_var.iloc[i, 0]]["Średni miesięczny dochód opodatkowany na osobę"].var()

    return pd.merge(data_frame1, df_var, on="Kod Jednostki Terytorialnej")


def weighted_average(data_frame_1, data_frame_2 ):

    df_solution = pd.DataFrame(
        columns=["Kod Jednostki Terytorialnej",
                 "Średnia ważona rocznego dochodu opodatkowanego jednostek podległych",
                 "Średnia ważona miesięcznego dochodu opodatkowanego jednostek podległych"]
        )

    df_solution["Kod Jednostki Terytorialnej"] = data_frame_1["Kod Jednostki Terytorialnej"]

    for i in range(len(df_solution)):

        weight = \
            data_frame_2[data_frame_2["Kod Jednostki Terytorialnej"].str[:len(df_solution.iloc[i, 0])]
                         == df_solution.iloc[i, 0]]["Liczba ludności pracującej"]

        total_population = \
            data_frame_1[data_frame_1["Kod Jednostki Terytorialnej"]
                         == df_solution.iloc[i, 0]]["Liczba ludności pracującej"]

        weight = weight / int(total_population)

        income_year = \
        data_frame_2[data_frame_2["Kod Jednostki Terytorialnej"].str[:len(df_solution.iloc[i, 0])]
                     == df_solution.iloc[i, 0]]["Średni roczny dochód opodatkowany na osobę"]

        df_solution.iloc[i, 1] = (income_year * weight).sum()

        income_month = \
            data_frame_2[data_frame_2["Kod Jednostki Terytorialnej"].str[:len(df_solution.iloc[i, 0])]
                         == df_solution.iloc[i, 0]]["Średni miesięczny dochód opodatkowany na osobę"]

        df_solution.iloc[i, 2] = (income_month * weight).sum()

    return pd.merge(data_frame_1, df_solution, on="Kod Jednostki Terytorialnej")


def weighted_average_diffrence(data_frame):

    data_frame["Różnica średnich rocznych"] = data_frame["Średni roczny dochód opodatkowany na osobę"] - \
                                              data_frame["Średnia ważona rocznego dochodu opodatkowanego jednostek podległych"]

    data_frame["Różnica średnich miesięcznych"] = data_frame["Średni miesięczny dochód opodatkowany na osobę"] - \
                                              data_frame["Średnia ważona miesięcznego dochodu opodatkowanego jednostek podległych"]

    return data_frame
