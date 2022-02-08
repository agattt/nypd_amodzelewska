
def add_difference(data_frame, year1, year2):

    data_frame[year2 + " - " + year1] = \
        data_frame["Dochód z PIT w " + year2] - \
        data_frame["Dochód z PIT w " + year1]

    return data_frame
