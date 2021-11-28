import csv


def create_data(input_file):

    data_raw = {}

    line_num = 0

    header = []

    with open(input_file, 'r') as data:

        csv_reader = csv.reader(data)

        for line in csv_reader:

            if line_num != 0:

                for i in range(len(header)):

                    data_raw[header[i]] = data_raw[header[i]] + [float(line[i])]

            else:

                header = line

                header.remove('variety')

                for elt in header:

                    data_raw[elt] = []

                line_num += 1

    return data_raw
