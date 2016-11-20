from src.feature_extraction.simple_stats import calculate_winner_range, calculate_winner, calculate_wins_percentage, calculate_wins_percentage_overall
from src.feature_extraction.points_features import calculate_average_points


def feature_extraction(data_frame):
    """
    :param data_frame: The loaded input file
    :return:
    """
    dict_list = list()
    # win/loss and margin win/loss - y column
    dict_list.append(calculate_winner(data_frame))
    dict_list.append(calculate_winner_range(data_frame))

    # average points per game
    dict_list.append(calculate_average_points(data_frame, "home"))
    dict_list.append(calculate_average_points(data_frame, "away"))

    # wins percentage
    dict_list.append(calculate_wins_percentage(data_frame, "home"))
    dict_list.append(calculate_wins_percentage(data_frame, "away"))

    return dict_list
