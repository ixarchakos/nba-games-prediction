import pandas
from src.feature_extraction.feature_extraction import feature_extraction
from src.tools.general_tools import merge_dicts


if __name__ == "__main__":
    df = pandas.read_csv('data/nba_games_2004_2005.csv')
    print feature_extraction(df)[1]
    print merge_dicts(df)
