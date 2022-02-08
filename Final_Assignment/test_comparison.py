
import pandas as pd
import package_pit.pit_assignment.comparison as cmp


def test_merge_jst_codes():

    assert cmp.merge_jst_codes("data/test/gminy_income.xlsx").equals(
           pd.Series(["0201011", "0201022", "0201032", "0201043", "0201052", "0201062"])), "Błąd w kodach gmin"

    assert cmp.merge_jst_codes("data/test/powiaty_income.xlsx").equals(pd.Series(["0201"])), "Błąd w kodach powiatów"

    assert cmp.merge_jst_codes("data/test/woj_income.xlsx").equals(pd.Series(["02"])), "Błąd w kodach województ"

    assert cmp.merge_jst_codes("data/test/miasta_income.xlsx").equals(pd.Series(["0261", "0261"])), "Błąd w kodach miast"


def test_create_data_frame():

    df = cmp.create_data_frame("data/test/gminy_income.xlsx", "2020")

    assert len(df) == 6, "Błąd tworzenia DataFrame dochodu dla gmin - zła liczba wierszy"

    assert len(df.columns) == 5, "Błąd tworzenia DataFrame dla dochodu gmin - zła liczba kolumn"

    df = cmp.create_data_frame("data/test/powiaty_income.xlsx", "2020")

    assert len(df) == 1, "Błąd tworzenia DataFrame dochodu dla powiatów - zła liczba wierszy"

    assert len(df.columns) == 5, "Błąd tworzenia DataFrame dla dochodu powiatów - zła liczba kolumn"

    df = cmp.create_data_frame("data/test/woj_income.xlsx", "2020")

    assert len(df) == 1, "Błąd tworzenia DataFrame dochodu dla województw - zła liczba wierszy"

    assert len(df.columns) == 5, "Błąd tworzenia DataFrame dla dochodu województw - zła liczba kolumn"

    df = cmp.create_data_frame("data/test/miasta_income.xlsx", "2020")

    assert len(df) == 2, "Błąd tworzenia DataFrame dochodu dla miast - zła liczba wierszy"

    assert len(df.columns) == 5, "Błąd tworzenia DataFrame dla dochodu miast - zła liczba kolumn"


def test_sum_rows():

    df = cmp.create_data_frame("data/test/miasta_income.xlsx", "2020")

    df = cmp.sum_rows(df, "2020")

    assert len(df) == 1, "Niepoprawna liczba wierszy po sumie dochodów dla miast"

    assert df.iloc[0]["Dochód z PIT w 2020"] == 103788614, "Niepoprawna suma dochodów dla miast"
