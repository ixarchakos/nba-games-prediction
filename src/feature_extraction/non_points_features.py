def non_points_features(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average fouls per game
    # dict_list.append(calculate_average_points(data_frame, "home"))
    # feature_name_list.append("calculate_average_home_points_home")
    # dict_list.append(calculate_average_points(data_frame, "away"))
    # feature_name_list.append("calculate_average_away_points_away")

    return dict_list, feature_name_list


def average_fouls(data_frame):
    """
    :param data_frame:
    :return:
    """
    total_games_dict, total_fouls_dict, percentage_home_dict, percentage_away_dict = dict(), dict(), dict(), dict()
    for index, row in data_frame.iterrows():

        # add calculated percentage in the feature dictionary
        if row['home_team'] not in total_games_dict:
            percentage_home_dict[row["id"]] = 0
        else:
            percentage_home_dict[row["id"]] = format(float(total_fouls_dict[row['home_team']]) / float(total_games_dict[row['home_team']]), '.2f')

        if row['away_team'] not in total_games_dict:
            percentage_away_dict[row["id"]] = 0
        else:
            percentage_away_dict[row["id"]] = format(float(total_fouls_dict[row['away_team']]) / float(total_games_dict[row['away_team']]), '.2f')

        # calculate teams' total games until now
        for team_name in ['home_team', 'away_team']:
            if row[team_name] in total_games_dict:
                total_games_dict[row[team_name]] += 1
            else:
                total_games_dict[row[team_name]] = 1

        # calculate teams' wins until now
        for team_name in ['home_team', 'away_team']:
            if row[team_name] in total_fouls_dict:
                total_fouls_dict[row[team_name]] += row['personal_fouls_'+team_name.split('_')[0]]
            else:
                total_fouls_dict[row[team_name]] = row['personal_fouls_'+team_name.split('_')[0]]

    return percentage_home_dict, percentage_away_dict
