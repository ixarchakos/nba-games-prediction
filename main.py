import pandas
from time import time

from src.tools.general_tools import merge_dicts, write_to_csv
from src.machine_learning.classification import do_classification


if __name__ == "__main__":

    feature_matrix = dict()
    start_time = time()
    print "*** Start feature extraction ***"
    for year in ['2004_2005', '2005_2006', '2006_2007', '2008_2009', '2009_2010',
                 '2010_2011', '2012_2013', '2013_2014', '2014_2015']:

        df = pandas.read_csv('data/nba_games_' + year + '.csv')
        feature_matrix.update(merge_dicts(df))

    print "*** The feature extraction ends after ", time() - start_time, " seconds ***"
    write_to_csv(feature_matrix)
    print "*** Start classification ***"
    do_classification()
