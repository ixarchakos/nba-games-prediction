def points_features(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average points per game
    dict_list.append(calculate_average_points(data_frame, "home"))
    feature_name_list.append("calculate_average_home_points_home")
    dict_list.append(calculate_average_points(data_frame, "away"))
    feature_name_list.append("calculate_average_away_points_away")

    # average points in paint per game
    avg_points_in_paint = averages(data_frame, 'points_in_paint_')
    dict_list.append(avg_points_in_paint[0])
    feature_name_list.append("points_in_paint_home")
    dict_list.append(avg_points_in_paint[1])
    feature_name_list.append("points_in_paint_away")

    # average points per game
    avg_points = averages(data_frame, '_points')
    dict_list.append(avg_points[0])
    feature_name_list.append("average_points_home")
    dict_list.append(avg_points[1])
    feature_name_list.append("average_points_away")

    # average allowed points per game
    dict_list.append(calculate_average_points_allowed(data_frame, "home"))
    feature_name_list.append("calculate_average_home_allowed_points_home")
    dict_list.append(calculate_average_points_allowed(data_frame, "away"))
    feature_name_list.append("calculate_average_away_allowed_points_away")

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


def averages(data_frame, feature):
    """
    :param data_frame:
    :param feature:
    :return:
    """
    total_games_dict, total_dict, percentage_home_dict, percentage_away_dict = dict(), dict(), dict(), dict()
    for index, row in data_frame.iterrows():

        # add calculated percentage in the feature dictionary
        if row['home_team'] not in total_games_dict:
            percentage_home_dict[row["id"]] = 0
        else:
            percentage_home_dict[row["id"]] = format(float(total_dict[row['home_team']]) / float(total_games_dict[row['home_team']]), '.2f')

        if row['away_team'] not in total_games_dict:
            percentage_away_dict[row["id"]] = 0
        else:
            percentage_away_dict[row["id"]] = format(float(total_dict[row['away_team']]) / float(total_games_dict[row['away_team']]), '.2f')

        # calculate teams' total games until now
        for team_name in ['home_team', 'away_team']:
            if row[team_name] in total_games_dict:
                total_games_dict[row[team_name]] += 1
            else:
                total_games_dict[row[team_name]] = 1

        # calculate teams' wins until now
        for team_name in ['home_team', 'away_team']:
            if row[team_name] in total_dict:
                if feature == '_points':
                    total_dict[row[team_name]] += row[team_name.split('_')[0] + feature]
                else:
                    total_dict[row[team_name]] += row[feature+team_name.split('_')[0]]
            else:
                if feature == '_points':
                    total_dict[row[team_name]] = row[team_name.split('_')[0] + feature]
                else:
                    total_dict[row[team_name]] = row[feature+team_name.split('_')[0]]

    return percentage_home_dict, percentage_away_dict


def calculate_average_points_allowed(data_frame, mode):
    """
    :param data_frame: The loaded input file
    :param mode:
    :return:
    """
    total_games_dict, total_points_dict, percentage_dict = dict(), dict(), dict()
    if mode == 'home':
        team_name = 'home_team'
        opponent_points = 'away_points'
    else:
        team_name = 'away_team'
        opponent_points = 'home_points'

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
            total_points_dict[row[team_name]] += row[opponent_points]
        else:
            total_points_dict[row[team_name]] = row[opponent_points]

    return percentage_dict
