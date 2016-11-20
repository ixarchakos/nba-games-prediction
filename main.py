from src.feature_extraction.simple_stats import calculate_winner_range
from src.feature_extraction.points_features import calculate_average_points
import pandas


def feature_extraction(data_frame):
    """
    :param data_frame:
    :return:
    """
    calculate_winner_range(data_frame)
    calculate_average_points(data_frame, "home")
    calculate_average_points(data_frame, "away")


def test_function(data_frame):
    for k, v in calculate_winner_range(data_frame).iteritems():
        print k, v
    print '*' * 100
    for k, v in calculate_average_points(data_frame, "home").iteritems():
        print k, v
    print '*' * 100
    for k, v in calculate_average_points(data_frame, "away").iteritems():
        print k, v


if __name__ == "__main__":
    df = pandas.read_csv('data/nba_games_2004_2005.csv')
    test_function(df)


