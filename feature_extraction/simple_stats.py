
def calculate_winner(home_points, away_points):
    """
    :param home_points: The total points of the home team
    :param away_points: The total points of the away team

    :return: Binary value: 1 if home team won else 0
    """
    return 1 if home_points > away_points else 0


def calculate_winner_range(home_points, away_points):
    """
    :param home_points: The total points of the home team
    :param away_points: The total points of the away team

    :return: Binary value: 1 if home team won else 0
    """
    if 0 <= home_points - away_points <= 6:
        return 1
    elif 7 <= home_points - away_points <= 15:
        return 2
    elif home_points - away_points > 15:
        return 3
    elif 0 <= away_points - home_points <= 6:
        return -1
    elif 7 <= away_points - home_points <= 15:
        return -2
    elif away_points - home_points > 15:
        return -3
