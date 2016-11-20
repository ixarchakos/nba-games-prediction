import pandas
import operator
from src.feature_extraction.simple_stats import calculate_winner_range, calculate_winner, calculate_wins_percentage
from src.feature_extraction.points_features import calculate_average_points


def feature_extraction(data_frame):
    """
    :param data_frame: The loaded input file
    :return:
    """
    dict_list = list()
    dict_list.append(calculate_winner(data_frame))
    dict_list.append(calculate_winner_range(data_frame))
    dict_list.append(calculate_average_points(data_frame, "home"))
    dict_list.append(calculate_average_points(data_frame, "away"))
    return dict_list


def test_function(data_frame):
    for k, v in sorted(calculate_wins_percentage(data_frame, 'home').items(), key=operator.itemgetter(0)):
        print k, v


def merge_dicts(data_frame):
    final_dict = dict()
    for d in feature_extraction(data_frame):
        for key, value in d.iteritems():
            final_dict.setdefault(key, []).append(value)


if __name__ == "__main__":
    df = pandas.read_csv('data/nba_games_2004_2005.csv')
    test_function(df)


