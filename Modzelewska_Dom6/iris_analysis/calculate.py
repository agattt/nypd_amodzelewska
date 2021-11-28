import statistics as stat


def calc_stats(dict_raw):

    dict_stats = {}

    for key in dict_raw:

        dict_stats[key] = [stat.mean(dict_raw[key]), stat.median(dict_raw[key]), stat.stdev(dict_raw[key])]

    return dict_stats
