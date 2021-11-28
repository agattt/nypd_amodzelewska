import csv


def create_output_file(dict_stat, output_file):

    with open(output_file, 'w', newline="") as output:

        csv_writer = csv.writer(output)

        csv_writer.writerow(["Parameter", "Mean", "Median", "Standard_Deviation"])

        for key in dict_stat:

            csv_writer.writerow([key] + dict_stat[key])
