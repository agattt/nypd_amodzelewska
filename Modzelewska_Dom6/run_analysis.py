import argparse
from iris_analysis.io.load import create_data
from iris_analysis.io.save import create_output_file
from iris_analysis.calculate import calc_stats


parser = argparse.ArgumentParser(description='Calculate statistics from data_file and export them into result_file')
parser.add_argument('data_file', help='Path of a data file')
parser.add_argument('result_file', help='Path to a result file')
args = parser.parse_args()


def main():

    data = create_data(args.data_file)
    data = calc_stats(data)
    create_output_file(data, args.result_file)


main()
