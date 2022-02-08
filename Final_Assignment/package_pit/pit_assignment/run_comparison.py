
from package_pit.pit_assignment.comparison.data_prep import create_data_frame
from package_pit.pit_assignment.comparison.data_prep import check_code_changes
from package_pit.pit_assignment.comparison.data_prep import join_data_frames
from package_pit.pit_assignment.comparison.data_prep import sum_rows
from package_pit.pit_assignment.comparison.difference import add_difference
from package_pit.pit_assignment.comparison.save import to_file


def compare(path_1, path_2, year_1, year_2, jst_type, output_file):

    if jst_type in ["Gminy", "Województwa", "Powiaty", "Miasta"]:

        df1 = create_data_frame(path_1, year_1)

        df2 = create_data_frame(path_2, year_2)

        if jst_type == "Miasta":

            df1 = sum_rows(df1, year_1)

            df2 = sum_rows(df2, year_2)

        check_code_changes(df1, df2, jst_type)

        df = join_data_frames(df1, df2)

        df = add_difference(df, year_1, year_2)

        to_file(df, year_1, year_2, output_file)

        return df

    else:

        return "Niepoprawny typ JST. Podaj jeden z: \"Gminy\", \"Województwa\", \"Powiaty\", \"Miasta\""
