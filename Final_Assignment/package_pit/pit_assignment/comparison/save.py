import pandas as pd


def to_file(data_frame, year1, year2, output_file):

    df1 = data_frame[data_frame[year2 + " - " + year1] > 0]
    df2 = data_frame[data_frame[year2 + " - " + year1] < 0]
    df3 = data_frame[data_frame[year2 + " - " + year1] == 0]

    with pd.ExcelWriter(output_file) as writer:

        if not df1.empty:

            df1.to_excel(writer, sheet_name="Większe dochody w " + year2, index=False)

        if not df2.empty:

            df2.to_excel(writer, sheet_name="Większe dochody w " + year1, index=False)

        if not df3.empty:

            df3.to_excel(writer, sheet_name="Dochody bez zmian", index=False)
