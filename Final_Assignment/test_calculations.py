
import package_pit.pit_assignment.comparison as cmp
import package_pit.pit_assignment.calculations as calc


def test_population_df():

    df = calc.population_df("data/test/pop_gmina.xls", 1)

    assert len(df.columns) == 3, "Niepoprawna liczba kolumn DataFrame dla populacji gmin"

    assert list(df["Liczba ludności pracującej"]) == [66848, 32365, 12040, 4421, 12309, 5853, 6969], \
        "Niepoprawna liczba ludnośći dla gmin"

    df = calc.population_df("data/test/pop_powiat.xls", 1)

    assert len(df.columns) == 3, "Niepoprawna liczba kolumn DataFrame dla populacji powiatów"

    assert list(df["Liczba ludności pracującej"]) == [66848, 73957], \
        "Niepoprawna liczba ludnośći dla powiatów"

    df = calc.population_df_województwa("data/test/pop_woj.xls", 1)

    assert len(df.columns) == 2, "Niepoprawna liczba kolumn DataFrame dla populacji województw"

    assert list(df["Liczba ludności pracującej"]) == [2393239], \
        "Niepoprawna liczba ludnośći dla województw"


def test_income_population():

    assert len( calc.income_population( cmp.create_data_frame( "data/test/gminy_income.xlsx", "2020"),
                                        calc.population_df("data/test/pop_gmina.xls",1)).columns) == 6, \
        "Niepoprawna liczba kolumn po połączeniu dochodu i danych populacyjnych dla gmin"

    assert len( calc.income_population( cmp.create_data_frame( "data/test/powiaty_income.xlsx", "2020"),
                                        calc.population_df("data/test/pop_powiat.xls", 1)).columns) == 6, \
        "Niepoprawna liczba kolumn po połączeniu dochodu i danych populacyjnych dla powiatów"

    assert len( calc.income_population_województwa( cmp.create_data_frame( "data/test/woj_income.xlsx", "2020"),
                                                    calc.population_df_województwa("data/test/pop_woj.xls", 1)).columns) == 6, \
        "Niepoprawna liczba kolumn po połączeniu dochodu i danych populacyjnych dla województw"

    assert len( calc.income_population(cmp.create_data_frame( "data/test/miasta_income.xlsx", "2020"),
                                        calc.population_df( "data/test/pop_powiat.xls", 1)).columns) == 6, \
        "Niepoprawna liczba kolumn po połączeniu dochodu i danych populacyjnych dla miast"


def test_taxed_income():

    df = calc.income_population(cmp.create_data_frame("data/test/gminy_income.xlsx", "2020"),
                                calc.population_df("data/test/pop_gmina.xls", 1)
                                )

    df = calc.taxed_income(df, "2020", 0.3816, 0.17)

    assert len(df.columns) == 10, \
        "Niepoprawna liczba kolumn po dodaniu średniego dochodu opodatkowanego dla gmin"

    assert list(df.iloc[0, 6:]) == \
           [40456699/32365, (40456699/32365)/0.3816, ((40456699/32365)/0.3816)/0.17, (((40456699/32365)/0.3816)/0.17)/12 ], \
            "Niepoprawne obliczenia średniego dochodu opodatkowanego dla gmin"

    df = calc.income_population(cmp.create_data_frame("data/test/powiaty_income.xlsx", "2020"),
                                calc.population_df("data/test/pop_powiat.xls", 1))

    df = calc.taxed_income(df, "2020", 0.1025, 0.17)

    assert len(df.columns) == 10, \
        "Niepoprawna liczba kolumn po dodaniu średniego dochodu opodatkowanego dla powiatów"

    assert list(df.iloc[0, 6:]) == \
           [21276533 / 73957, (21276533 / 73957) / 0.1025, ((21276533 / 73957) / 0.1025) / 0.17,
            (((21276533 / 73957) / 0.1025) / 0.17) / 12], \
        "Niepoprawne obliczenia średniego dochodu opodatkowanego dla powiatów"

    df = calc.income_population_województwa(cmp.create_data_frame("data/test/woj_income.xlsx", "2020"),
                                calc.population_df_województwa("data/test/pop_woj.xls", 1))

    df = calc.taxed_income(df, "2020", 0.016, 0.17)

    assert len(df.columns) == 10, \
        "Niepoprawna liczba kolumn po dodaniu średniego dochodu opodatkowanego dla województw"

    assert list(df.iloc[0, 6:]) == \
           [143787146 / 2393239, (143787146 / 2393239) / 0.016, ((143787146 / 2393239) / 0.016) / 0.17,
            (((143787146 / 2393239) / 0.016) / 0.17) / 12], \
        "Niepoprawne obliczenia średniego dochodu opodatkowanego dla województw"

    df = calc.income_population(
        cmp.sum_rows(cmp.create_data_frame("data/test/miasta_income.xlsx", "2020"), "2020"),
        calc.population_df("data/test/pop_powiat.xls", 1)
    )

    df = calc.taxed_income(df, "2020", 0.1185, 0.17)

    assert len(df.columns) == 10, "Niepoprawna liczba kolumn po dodaniu średniego dochodu opodatkowanego dla miast"

    assert list(df.iloc[0, 6:]) == \
           [103788614 / 66848, (103788614 / 66848) /  0.1185, ((103788614 / 66848) /  0.1185) / 0.17,
            (((103788614/ 66848) /  0.1185) / 0.17) / 12], \
        "Niepoprawne obliczenia średniego dochodu opodatkowanego dla miast"


def test_variance():

    df1 = calc.income_population(
                                cmp.create_data_frame("data/test/powiaty_income.xlsx", "2020"),
                                calc.population_df("data/test/pop_powiat.xls", 1)
                                )

    df1 = calc.taxed_income(df1, "2020", 0.1025, 17)

    df2 = calc.income_population(cmp.create_data_frame("data/test/gminy_income.xlsx", "2020"),
                                calc.population_df("data/test/pop_gmina.xls", 1)
                                )

    df2 = calc.taxed_income(df2, "2020", 0.3816, 0.17)

    assert list(calc.variance(df1, df2, "2020")["Wariancja średniego rocznego dochodu w podległych JST"]) == \
        df2["Średni roczny dochód opodatkowany na osobę"].var(), \
        "Nieprawidłowa wariancja średnich rocznych dochodów opodatkowanych dla powiatów"

    assert list(calc.variance(df1, df2, "2020")["Wariancja średniego miesięcznego dochodu w podległych JST"]) == \
        df2["Średni miesięczny dochód opodatkowany na osobę"].var(), \
        "Nieprawidłowa wariancja średnich miesięcznych dochodów opodatkowanych dla powiatów"


def test_weighted_average():

    df1 = calc.income_population(
        cmp.create_data_frame("data/test/powiaty_income.xlsx", "2020"),
        calc.population_df("data/test/pop_powiat.xls", 1)
    )

    df1 = calc.taxed_income(df1, "2020", 0.1025, 17)

    df2 = calc.income_population(cmp.create_data_frame("data/test/gminy_income.xlsx", "2020"),
                                 calc.population_df("data/test/pop_gmina.xls", 1)
                                 )

    df2 = calc.taxed_income(df2, "2020", 0.3816, 0.17)

    assert round(float(calc.weighted_average(df1, df2)["Średnia ważona rocznego dochodu opodatkowanego jednostek podległych"]), 2) == \
           16510.05, \
           "Nieprawidłowa średnia ważona rocznych dochodów opodatkowanych dla powiatów"

    assert round(float(calc.weighted_average(df1, df2)["Średnia ważona miesięcznego dochodu opodatkowanego jednostek podległych"]), 2) == \
           1375.84, \
           "Nieprawidłowa średnia ważona miesięcznych dochodów opodatkowanych dla powiatów"
