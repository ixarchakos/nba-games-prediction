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
            percentage_dict[row["id"]] = float(total_points_dict[row[team_name]]) / float(total_games_dict[row[team_name]])

        if row[team_name] in total_games_dict:
            total_games_dict[row[team_name]] += 1
        else:
            total_games_dict[row[team_name]] = 1

        if row[team_name] in total_points_dict:
            total_points_dict[row[team_name]] += row[team_points]
        else:
            total_points_dict[row[team_name]] = row[team_points]

    return percentage_dict
