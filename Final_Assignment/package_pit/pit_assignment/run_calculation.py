from package_pit.pit_assignment.calculations.data_prep import population_df
from package_pit.pit_assignment.calculations.data_prep import population_df_województwa
from package_pit.pit_assignment.calculations.data_merge import income_population
from package_pit.pit_assignment.calculations.data_merge import income_population_województwa
from package_pit.pit_assignment.calculations.calculate import taxed_income
from package_pit.pit_assignment.calculations.calculate import variance
from package_pit.pit_assignment.calculations.calculate import weighted_average
from package_pit.pit_assignment.calculations.save import to_file
from package_pit.pit_assignment.calculations.calculate import weighted_average_diffrence


def run_taxed_income(path_population, paying_percentage, df_income, jst_type, jst_share, tax_threshold, output_file):

    if jst_type == "Województwa":

        df_pop = population_df_województwa(path_population, paying_percentage)

        df_solution = income_population_województwa(df_income, df_pop)

    else:

        df_pop = population_df(path_population, paying_percentage)

        df_solution = income_population(df_income, df_pop)

    df_solution = taxed_income(df_solution, "2020", jst_share, tax_threshold)

    to_file(output_file, df_solution, "Średni dochód opodatkowany")

    return df_solution


def run_variance(data_frame_1, data_frame_2, year, output_file):

    df_solution = variance(data_frame_1, data_frame_2, year)

    to_file(output_file, df_solution, "Wariancja w podległych JST")

    return df_solution


def run_weighted_average(data_frame_1, data_frame_2, output_file):

    df_solution = weighted_average(data_frame_1, data_frame_2)

    df_solution = weighted_average_diffrence(df_solution)

    to_file(output_file, df_solution, "Średnia ważona")

    return df_solution
