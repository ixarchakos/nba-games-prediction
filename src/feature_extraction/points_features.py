def calculate_home_average_points(total_home_games_dict, total_home_points_dict, team_name, home_points):
    """
    :param total_home_games_dict:
    :param total_home_points_dict:
    :param team_name:
    :param home_points:

    :return:
    """
    if team_name in total_home_games_dict:
        total_home_games_dict[team_name] += 1
    else:
        total_home_games_dict[team_name] = 1

    if team_name in total_home_points_dict:
        total_home_points_dict[team_name] += home_points
    else:
        total_home_points_dict[team_name] = home_points

    percentage = float(total_home_points_dict[team_name])/float(total_home_games_dict[team_name])

    return total_home_games_dict, total_home_points_dict, percentage