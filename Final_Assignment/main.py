from package_pit.pit_assignment.run_comparison import compare
from package_pit.pit_assignment.run_calculation import run_taxed_income
from package_pit.pit_assignment.comparison.data_prep import create_data_frame
from package_pit.pit_assignment.comparison.data_prep import sum_rows
from package_pit.pit_assignment.run_calculation import run_variance
from package_pit.pit_assignment.run_calculation import run_weighted_average
import pandas as pd


def run_all(path_gminy_1, path_gminy_2, path_gminy_pop,
            path_powiaty_1, path_powiaty_2, path_powiaty_pop,
            path_woj_1, path_woj_2, path_woj_pop,
            path_miasta_1, path_miasta_2,
            year_1, year_2,
            output_gminy, output_powiaty,
            output_miasta, output_woj,
            share_gminy_2, share_powiat,
            share_woj, share_miasta_2,
            tax_threshold, paying_percentage
            ):

    compare(path_gminy_1, path_gminy_2, year_1, year_2, "Gminy", output_gminy)

    compare(path_powiaty_1, path_powiaty_2, year_1, year_2, "Powiaty", output_powiaty)

    compare(path_woj_1, path_woj_2, year_1, year_2, "Województwa", output_woj)

    compare(path_miasta_1, path_miasta_2, year_1, year_2, "Miasta", output_miasta)

    writer_gminy = pd.ExcelWriter(output_gminy,
                                  mode="a",
                                  engine="openpyxl")

    writer_powiaty = pd.ExcelWriter(output_powiaty,
                                    mode="a",
                                    engine="openpyxl")

    writer_województwa = pd.ExcelWriter(output_woj,
                                        mode="a",
                                        engine="openpyxl")

    writer_miasta = pd.ExcelWriter(output_miasta,
                                   mode="a",
                                   engine="openpyxl")

    df_gminy_2 = create_data_frame(path_gminy_2, year_2)

    df_gminy_income = run_taxed_income(path_gminy_pop, paying_percentage,
                                       df_gminy_2, "Gminy", share_gminy_2,
                                       tax_threshold, writer_gminy)

    writer_gminy.save()

    df_powiaty_2 = create_data_frame(path_powiaty_2, year_2)

    df_powiaty_income = run_taxed_income(path_powiaty_pop, paying_percentage,
                                         df_powiaty_2, "Powiaty", share_powiat,
                                         tax_threshold, writer_powiaty)

    df_woj_2 = create_data_frame(path_woj_2, year_2)

    df_woj_income = run_taxed_income(path_woj_pop, paying_percentage,
                                     df_woj_2, "Województwa", share_woj,
                                     tax_threshold, writer_województwa)

    df_miasta_2 = sum_rows(create_data_frame(path_miasta_2, year_2), year_2)

    run_taxed_income(path_powiaty_pop, paying_percentage,
                     df_miasta_2, "Miasta", share_miasta_2,
                     tax_threshold, writer_miasta)

    writer_miasta.save()

    run_variance(df_powiaty_2, df_gminy_2, year_2, writer_powiaty)

    run_variance(df_woj_2, df_powiaty_2, year_2, writer_województwa)

    run_weighted_average(df_powiaty_income, df_gminy_income, writer_powiaty)

    writer_powiaty.save()

    run_weighted_average(df_woj_income, df_powiaty_income, writer_województwa)

    writer_województwa.save()
