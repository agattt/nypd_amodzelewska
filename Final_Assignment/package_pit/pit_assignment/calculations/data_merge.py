import pandas as pd


def income_population(data_frame_income, data_frame_population):

    return pd.merge(data_frame_income, data_frame_population[["Kod Jednostki Terytorialnej", "Liczba ludności pracującej"]], on="Kod Jednostki Terytorialnej")


def income_population_województwa(data_frame_income, data_frame_population):

    return pd.merge(data_frame_income, data_frame_population, on="Nazwa JST")
