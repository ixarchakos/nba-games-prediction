from src.feature_extraction.points_features import calculate_average_points


def advanced_statistics(data_frame):
    dict_list = list()
    feature_name_list = list()

    # average possessions per game
    avg_possessions = possessions_overall(data_frame)
    dict_list.append(avg_possessions[0])
    feature_name_list.append("average_possessions_home")
    dict_list.append(avg_possessions[1])
    feature_name_list.append("average_possessions_away")

    # average home and away possessions per game
    dict_list.append(possessions_home_away(data_frame, 'home'))
    feature_name_list.append("average_home_possessions_home")
    dict_list.append(possessions_home_away(data_frame, 'away'))
    feature_name_list.append("average_away_possessions_away")

    # average home and away offensive rating
    dict_list.append(offensive_rating(data_frame, 'home'))
    feature_name_list.append("home_offensive_rating_home")
    dict_list.append(offensive_rating(data_frame, 'away'))
    feature_name_list.append("away_offensive_rating_away")

    return dict_list, feature_name_list


def possessions_overall(data_frame):
    """
    :param data_frame:
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

            possessions = int(row[fga + team_name.split('_')[0]].split('-')[1]) - int(row[orb + team_name.split('_')[0]]) + \
                             (0.475 * int(row[fta + team_name.split('_')[0]].split('-')[1])) + int(row[to + team_name.split('_')[0]])

            if row[team_name] in total_dict:
                total_dict[row[team_name]] += possessions
            else:
                total_dict[row[team_name]] = possessions

    return percentage_home_dict, percentage_away_dict


def possessions_home_away(data_frame, mode):
    """
    This feature calculates the total home possessions per game for the home team and the away possessions per game for the away team,
    according to how the mode variable has set
    :param data_frame: The loaded input file
    :param mode: string binary variable
    :return: dict
    """
    total_games_dict, total_dict, percentage_dict = dict(), dict(), dict()
    team_name = 'home_team' if mode == 'home' else 'away_team'
    for index, row in data_frame.iterrows():
        if row[team_name] not in total_games_dict:
            percentage_dict[row["id"]] = 0
        else:
            percentage_dict[row["id"]] = format(float(total_dict[row[team_name]]) / float(total_games_dict[row[team_name]]), '.2f')

        if row[team_name] in total_games_dict:
            total_games_dict[row[team_name]] += 1
        else:
            total_games_dict[row[team_name]] = 1

        fga, orb, fta, to = 'fg_made_attempted_', 'offensive_rebounds_', 'ft_made_attempted_', 'turnovers_'

        possessions = int(row[fga + team_name.split('_')[0]].split('-')[1]) - int(row[orb + team_name.split('_')[0]]) + \
                         (0.475 * int(row[fta + team_name.split('_')[0]].split('-')[1])) + int(row[to + team_name.split('_')[0]])

        if row[team_name] in total_dict:
            total_dict[row[team_name]] += possessions
        else:
            total_dict[row[team_name]] = possessions

    return percentage_dict


def offensive_rating(data_frame, mode):
    """
    This feature calculates the offensive rating for the home team and the offensive rating for the away team,
    according to how the mode variable has set. It utilizes the features possessions_home_away and calculate_average_points
    :param data_frame: The loaded input file
    :param mode: string binary variable
    :return: dict
    """
    off_rat = dict()
    average_points = calculate_average_points(data_frame, mode)
    for k, possessions in possessions_home_away(data_frame, mode).items():
        try:
            off_rat[k] = format(float(average_points[k]) * 100 / float(possessions), '.2f')
        except ZeroDivisionError:
            off_rat[k] = 0.0
    return off_rat
