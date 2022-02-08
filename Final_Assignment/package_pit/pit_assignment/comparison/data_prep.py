import pandas as pd


def merge_jst_codes(data_file):

    data_codes = pd.read_excel(
        data_file, usecols=range(4),
        skiprows=range(7), header=None,
        dtype=str
    )

    list_of_codes = []

    for i in range(len(data_codes)):

        string = data_codes.iloc[i].str.cat()

        string = string.replace("-", "")

        list_of_codes.append(string)

    return pd.Series(list_of_codes)


def create_data_frame(data_file, year):

    data = pd.read_excel(data_file,
                         header=None,
                         usecols=[4, 5, 6, 10],
                         skiprows=range(7),
                         names=["Nazwa JST", "Województwo", "Powiat", "Dochód z PIT w " + year]
                         )

    data.insert(0, column="Kod Jednostki Terytorialnej", value=merge_jst_codes(data_file))

    return data


def check_code_changes(data_frame_1, data_frame_2, jst_type):

    df = pd.merge(data_frame_1.iloc[:, :2],
                  data_frame_2.iloc[:, :2],
                  on="Kod Jednostki Terytorialnej"
                  )

    rows = df.index[df["Nazwa JST_x"] != df["Nazwa JST_y"]]

    if len(rows) == 0:

        print("Między latami nie nastąpiły zmiany kodów jednostek terytorialnych")

    else:

        df = df.iloc[rows]

        df.to_excel("changed_codes.xlsx", sheet_name=jst_type)

        data_frame_1.drop(
            data_frame_1.index[data_frame_1["Kod Jednostki Terytorialnej"].isin(df["Kod Jednostki Terytorialnej"])],
            inplace=True
        )

        data_frame_2.drop(
            data_frame_2.index[data_frame_2["Kod Jednostki Terytorialnej"].isin(df["Kod Jednostki Terytorialnej"])],
            inplace=True
        )

        print("Wykryto zmiany kodów JST. Szczegóły zobacz w pliku \"changed_codes.xlsx\"")


def sum_rows(data_frame, year):

    lst = list(data_frame.columns)

    lst.remove("Dochód z PIT w " + year)

    return data_frame.groupby(by=lst, as_index=False).sum()


def join_data_frames(data_frame1, data_frame2):

    return pd.merge(data_frame1,
                    data_frame2.iloc[:, [0, 4]],
                    on=["Kod Jednostki Terytorialnej"]
                    )
