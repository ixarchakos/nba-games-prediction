
def calculate_winner(data_frame):
    """
    :param data_frame: The loaded input file
    :return:
    """
    games_dict = dict()
    for index, row in data_frame.iterrows():
        games_dict[row["id"]] = 1 if row["home_points"] > row["away_points"] else 0
    return games_dict


def calculate_winner_range(data_frame):
    """
    :param data_frame: The loaded input file
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


def calculate_wins_percentage(data_frame, mode):
    """
    :param data_frame: The loaded input file
    :param mode:
    :return:
    """
    total_games_dict, total_wins_dict, percentage_dict = dict(), dict(), dict()
    team_name = 'home_team' if mode == 'home' else 'away_team'
    for index, row in data_frame.iterrows():
        if row[team_name] not in total_games_dict:
            percentage_dict[row["id"]] = 0
        else:
            percentage_dict[row["id"]] = float(total_wins_dict[row[team_name]])/float(total_games_dict[row[team_name]])

        if row[team_name] in total_games_dict:
            total_games_dict[row[team_name]] += 1
        else:
            total_games_dict[row[team_name]] = 1

        if row[team_name] in total_wins_dict:
            if team_name == 'home_team':
                total_wins_dict[row[team_name]] += 1 if row['home_points'] > row['away_points'] else 0
            else:
                total_wins_dict[row[team_name]] += 1 if row['away_points'] > row['home_points'] else 0
        else:
            if team_name == 'home_team':
                total_wins_dict[row[team_name]] = 1 if row['home_points'] > row['away_points'] else 0
            else:
                total_wins_dict[row[team_name]] = 1 if row['away_points'] > row['home_points'] else 0

    return percentage_dict
