import pandas
import multiprocessing

from time import time
from src.feature_extraction.feature_extraction import merge_dicts
from src.tools.general_tools import  write_to_csv
from src.machine_learning.classification import do_classification


def process(total_years):
    """
    :param total_years: dict, required
    :return:
    """
    df = pandas.read_csv('data/nba_games_' + total_years + '.csv')
    extraction = merge_dicts(df, total_years)
    value_list = extraction[0]
    # extraction[1]
    return value_list


if __name__ == "__main__":

    feature_matrix = dict()
    start_time = time()
    print "*** Start feature extraction ***"
    years = ['2002_2003', '2003_2004', '2004_2005', '2005_2006', '2006_2007', '2007_2008',
             '2008_2009', '2009_2010', '2010_2011', '2011_2012', '2012_2013', '2013_2014',
             '2014_2015', '2015_2016']
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    results = pool.map(process, years)
    pool.close()
    for result in results:
        feature_matrix.update(result)
    print "*** The feature extraction ends after ", time() - start_time, " seconds ***"
    write_to_csv(feature_matrix)
    print "*** Start classification ***"
    do_classification()
