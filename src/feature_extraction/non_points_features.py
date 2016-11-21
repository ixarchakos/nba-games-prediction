def non_points_features(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average fouls per game
    avg_fouls = averages(data_frame, 'personal_fouls_')
    dict_list.append(avg_fouls[0])
    feature_name_list.append("average_fouls_home")
    dict_list.append(avg_fouls[1])
    feature_name_list.append("average_fouls_away")

    return dict_list, feature_name_list


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
                total_dict[row[team_name]] += row[feature+team_name.split('_')[0]]
            else:
                total_dict[row[team_name]] = row[feature+team_name.split('_')[0]]

    return percentage_home_dict, percentage_away_dict
