import pandas as pd


def population_df(data_file, paying_percentage):

    data_input = pd.ExcelFile(data_file)

    df_solution = pd.DataFrame(
        columns=["Nazwa JST", "Kod Jednostki Terytorialnej", "Liczba ludności pracującej"]
        )

    for i in range(len(data_input.sheet_names)):

        df_population = pd.read_excel(data_input,
                             sheet_name=i,
                             header=None,
                             usecols=range(3),
                             skiprows=range(8),
                             dtype={0: str, 1:str, 2:int},
                             names=["Nazwa JST", "Kod Jednostki Terytorialnej", "Liczba ludności pracującej"])

        if df_population.isnull().values.any() == True:

            df_population.fillna("", inplace=True)

        df_population["Kod Jednostki Terytorialnej"] = df_population["Kod Jednostki Terytorialnej"].str.replace(" ", "")

        df_population["Nazwa JST"] = df_population["Nazwa JST"].str.replace(" ", "")

        population = \
            (df_population[df_population["Nazwa JST"] == "Wiekprodukcyjny"]["Liczba ludności pracującej"]).reset_index(drop=True) + \
            (df_population[df_population["Nazwa JST"] == "Wiekpoprodukcyjny"]["Liczba ludności pracującej"].reset_index(drop=True))

        df_population = df_population[(df_population["Kod Jednostki Terytorialnej"] != "")].reset_index(drop=True)

        df_population["Liczba ludności pracującej"] = population*paying_percentage

        df_solution = pd.concat([df_solution, df_population])

    return df_solution


def population_df_województwa(data_file, paying_percentage):

    data_input = pd.ExcelFile(data_file)

    lst_województwa = list(data_input.sheet_names)

    df_solution = pd.DataFrame(
        columns=["Nazwa JST", "Liczba ludności pracującej"]
        )

    for i in range(len(data_input.sheet_names)):

        df_population = pd.read_excel(data_input,
                                      sheet_name=i,
                                      header=None,
                                      usecols=range(2),
                                      skiprows=range(8),
                                      dtype={0:str},
                                      names=["Nazwa JST", "Liczba ludności pracującej"])

        if df_population.isnull().values.any() == True:

            df_population.fillna("", inplace=True)

        df_population["Nazwa JST"] = df_population["Nazwa JST"].str.split("\n").str.get(0).str.replace(" ", "")

        population = \
            int(df_population[df_population["Nazwa JST"] == "Wiekprodukcyjny"]["Liczba ludności pracującej"]) + \
            int(df_population[df_population["Nazwa JST"] == "Wiekpoprodukcyjny"]["Liczba ludności pracującej"])

        df_population = df_population[(df_population["Nazwa JST"].isin(lst_województwa))].reset_index(drop=True)

        df_population["Liczba ludności pracującej"] = population*paying_percentage

        df_population["Nazwa JST"] = df_population["Nazwa JST"].str.lower()

        df_solution = pd.concat([df_solution, df_population])

    return df_solution
