from src.feature_extraction.simple_stats import calculate_winner_range
from src.feature_extraction.points_features import calculate_home_average_points
import pandas


if __name__ == "__main__":
    # dicts
    total_home_games_dict = dict()
    total_home_points_dict = dict()

    data_frame = pandas.read_csv('data/nba_games_2004_2005.csv')
    for index, row in data_frame.iterrows():
        # print index, calculate_winner_range(row['home_points'], row['away_points'])
        total_home_games_dict, total_home_points_dict, percentage = \
            calculate_home_average_points(total_home_games_dict, total_home_points_dict,
                                          row['home_team'], row['home_points'])
        print row['home_team'], percentage
