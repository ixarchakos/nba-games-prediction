def simple_stats(data_frame):
    """
    :return:
    """
    dict_list = list()
    feature_name_list = list()

    # win/loss and margin win/loss - y column
    dict_list.append(calculate_winner(data_frame))
    feature_name_list.append("calculate_winner")
    dict_list.append(calculate_winner_range(data_frame))
    feature_name_list.append("calculate_winner_range")

    # wins percentage
    dict_list.append(calculate_wins_percentage(data_frame, "home"))
    feature_name_list.append("calculate_home_wins_percentage_home")
    dict_list.append(calculate_wins_percentage(data_frame, "away"))
    feature_name_list.append("calculate_away_wins_percentage_away")
    dict_list.append(calculate_wins_percentage_overall(data_frame)[0])
    feature_name_list.append("calculate_wins_percentage_overall_home")
    dict_list.append(calculate_wins_percentage_overall(data_frame)[1])
    feature_name_list.append("calculate_wins_percentage_overall_away")

    return dict_list, feature_name_list


def calculate_winner(data_frame):
    """
    :param data_frame: The loaded input file
    :return: dict
    """
    games_dict = dict()
    for index, row in data_frame.iterrows():
        games_dict[row["id"]] = 1 if row["home_points"] > row["away_points"] else 0
    return games_dict


def calculate_winner_range(data_frame):
    """
    :param data_frame: The loaded input file
    :return: dict
    """
    games_dict = dict()
    teams = dict()
    i = 0
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
        if row["home_team"] not in teams:
            teams[row["home_team"]] = i
            i += 1
        if row["away_team"] not in teams:
            teams[row["away_team"]] = i
            i += 1

    return games_dict


def calculate_wins_percentage(data_frame, mode):
    """
    This feature calculates the total home win percentage for the home team and the away win percentage for the away team,
    regardless how the mode variable has set
    :param data_frame: The loaded input file
    :param mode: string binary variable
    :return: dict
    """
    total_games_dict, total_wins_dict, percentage_dict = dict(), dict(), dict()
    team_name = 'home_team' if mode == 'home' else 'away_team'
    for index, row in data_frame.iterrows():
        if row[team_name] not in total_games_dict:
            percentage_dict[row["id"]] = 0
        else:
            percentage_dict[row["id"]] = format(float(total_wins_dict[row[team_name]])/float(total_games_dict[row[team_name]]), '.2f')

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


def calculate_wins_percentage_overall(data_frame):
    """
    This feature calculates the total win percentage for both of the teams before the current game
    :param data_frame: The loaded input file
    :return:
    """
    total_games_dict, total_wins_dict, percentage_home_dict, percentage_away_dict = dict(), dict(), dict(), dict()
    for index, row in data_frame.iterrows():

        # add calculated percentage in the feature dictionary
        if row['home_team'] not in total_games_dict:
            percentage_home_dict[row["id"]] = 0
        else:
            percentage_home_dict[row["id"]] = format(float(total_wins_dict[row['home_team']]) / float(total_games_dict[row['home_team']]), '.2f')

        if row['away_team'] not in total_games_dict:
            percentage_away_dict[row["id"]] = 0
        else:
            percentage_away_dict[row["id"]] = format(float(total_wins_dict[row['away_team']]) / float(total_games_dict[row['away_team']]), '.2f')

        # calculate teams' total games until now
        if row['home_team'] in total_games_dict:
            total_games_dict[row['home_team']] += 1
        else:
            total_games_dict[row['home_team']] = 1

        if row['away_team'] in total_games_dict:
            total_games_dict[row['away_team']] += 1
        else:
            total_games_dict[row['away_team']] = 1

        # calculate teams' wins until now
        if row['home_team'] in total_wins_dict:
            total_wins_dict[row['home_team']] += 1 if row['home_points'] > row['away_points'] else 0
        else:
            total_wins_dict[row['home_team']] = 1 if row['home_points'] > row['away_points'] else 0

        if row['away_team'] in total_wins_dict:
            total_wins_dict[row['away_team']] += 1 if row['away_points'] > row['home_points'] else 0
        else:
            total_wins_dict[row['away_team']] = 1 if row['away_points'] > row['home_points'] else 0

    return percentage_home_dict, percentage_away_dict
