def advanced_statistics(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average possessions per game
    avg_possessions = possessions_overall(data_frame)
    dict_list.append(avg_possessions[0])
    feature_name_list.append("average_possessions_home")
    dict_list.append(avg_possessions[1])
    feature_name_list.append("average_possessions_away")


def possessions_overall(data_frame):
    """
    :param data_frame:
    :param mode:
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

        # calculate teams' possessions until now

        for team_name in ['home_team', 'away_team']:
            fga, orb, fta, to = 'fg_made_attempted_', 'offensive_rebounds_', 'ft_made_attempted_', 'turnovers_'
            possessions = 0.96 * (row[fga + team_name.split('_')[0]].split('-')[1] - row[orb + team_name.split('_')[0]] +
                                  (0.44 * row[fta + team_name.split('_')[0]].split('-')[1]) + row[to + team_name.split('_')[0]])
            if row[team_name] in total_dict:
                total_dict[row[team_name]] += possessions
            else:
                total_dict[row[team_name]] = possessions

    return percentage_home_dict, percentage_away_dict
