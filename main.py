import pandas
from src.feature_extraction.feature_extraction import feature_extraction


def merge_dicts(data_frame):
    final_dict = dict()
    for d in feature_extraction(data_frame):
        for key, value in d.iteritems():
            final_dict.setdefault(key, []).append(value)
    return final_dict

if __name__ == "__main__":
    df = pandas.read_csv('data/nba_games_2004_2005.csv')
    print merge_dicts(df)
