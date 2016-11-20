def point_features(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average points per game
    dict_list.append(calculate_average_points(data_frame, "home"))
    feature_name_list.append("calculate_average_home_points_home")
    dict_list.append(calculate_average_points(data_frame, "away"))
    feature_name_list.append("calculate_average_away_points_away")

    return dict_list, feature_name_list


def calculate_average_points(data_frame, mode):
    """
    :param data_frame: The loaded input file
    :param mode:
    :return:
    """
    total_games_dict, total_points_dict, percentage_dict = dict(), dict(), dict()
    if mode == 'home':
        team_name = 'home_team'
        team_points = 'home_points'
    else:
        team_name = 'away_team'
        team_points = 'away_points'

    for index, row in data_frame.iterrows():
        if row[team_name] not in total_games_dict:
            percentage_dict[row["id"]] = 0
        else:
            percentage_dict[row["id"]] = format(float(total_points_dict[row[team_name]]) / float(total_games_dict[row[team_name]]), '.2f')

        if row[team_name] in total_games_dict:
            total_games_dict[row[team_name]] += 1
        else:
            total_games_dict[row[team_name]] = 1

        if row[team_name] in total_points_dict:
            total_points_dict[row[team_name]] += row[team_points]
        else:
            total_points_dict[row[team_name]] = row[team_points]

    return percentage_dict
