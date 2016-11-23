def non_points_features(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average fouls per game
    avg_fouls = averages(data_frame, 'personal_fouls_')
    dict_list.append(avg_fouls[0])
    feature_name_list.append("average_fouls_home")
    dict_list.append(avg_fouls[1])
    feature_name_list.append("average_fouls_away")

    # average fast break points per game
    avg_fast_break_points = averages(data_frame, 'fast_break_points_')
    dict_list.append(avg_fast_break_points[0])
    feature_name_list.append("fast_break_points_home")
    dict_list.append(avg_fast_break_points[1])
    feature_name_list.append("fast_break_points_away")

    # average steals per game
    avg_steals = averages(data_frame, 'steals_')
    dict_list.append(avg_steals[0])
    feature_name_list.append("average_steals_home")
    dict_list.append(avg_steals[1])
    feature_name_list.append("average_steals_away")

    # average blocks per game
    avg_blocks = averages(data_frame, 'blocks_')
    dict_list.append(avg_blocks[0])
    feature_name_list.append("average_blocks_home")
    dict_list.append(avg_blocks[1])
    feature_name_list.append("average_blocks_away")

    # technical_fouls_
    avg_technical_fouls = averages(data_frame, 'technical_fouls_')
    dict_list.append(avg_technical_fouls[0])
    feature_name_list.append("average_technical_fouls_home")
    dict_list.append(avg_technical_fouls[1])
    feature_name_list.append("average_technical_fouls_away")

    # consecutive away games
    cag = consecutive_away_games(data_frame)
    dict_list.append(cag[0])
    feature_name_list.append("consecutive_away_games_home")
    dict_list.append(cag[1])
    feature_name_list.append("consecutive_away_games_away")

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


def consecutive_away_games(data_frame):
    """
    :param data_frame:
    :return:
    """
    final_home_dict, final_away_dict, total_dict = dict(), dict(), dict()
    for index, row in data_frame.iterrows():
        if row['home_team'] not in total_dict:
            final_home_dict[row["id"]] = 0
        else:
            final_home_dict[row["id"]] = total_dict[row['home_team']]

        if row['away_team'] not in total_dict:
            final_away_dict[row["id"]] = 0
        else:
            final_away_dict[row["id"]] = total_dict[row['away_team']]

        total_dict[row['home_team']] = 0
        if row['away_team'] not in total_dict:
            total_dict[row['away_team']] = 1
        else:
            total_dict[row['away_team']] += 1

    return final_home_dict, final_away_dict
