from src.feature_extraction.simple_stats import calculate_winner_range
import pandas
data_frame = pandas.read_csv('data/nba_games_2004_2005.csv')
for index, row in data_frame.iterrows():
    print index, calculate_winner_range(row['home_points'], row['away_points'])
