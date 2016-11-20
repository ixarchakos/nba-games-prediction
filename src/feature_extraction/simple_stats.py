
def calculate_winner(data_frame):
    """
    :param data_frame:
    :return:
    """
    games_dict = dict()
    for index, row in data_frame.iterrows():
        games_dict[row["id"]] = 1 if row["home_points"] > row["away_points"] else 0
    return games_dict


def calculate_winner_range(data_frame):
    """
    :param data_frame:
    :return:
    """
    games_dict = dict()
    for index, row in data_frame.iterrows():
        if 0 <= row["home_points"] - row["away_points"] <= 6:
            games_dict[row["id"]] = 1
        elif 7 <= row["home_points"] - row["away_points"] <= 15:
            games_dict[row["id"]] = 2
        elif row["home_points"] - row["away_points"] > 15:
            games_dict[row["id"]] = 3
        elif 0 <= row["away_points"] - row["home_points"] <= 6:
            games_dict[row["id"]] = -1
        elif 7 <= row["away_points"] - row["home_points"] <= 15:
            games_dict[row["id"]] = -2
        elif row["away_points"] - row["home_points"] > 15:
            games_dict[row["id"]] = -3
    return games_dict
