from multiprocessing import Pool, cpu_count
from pandas import read_csv
from src.feature_extraction.feature_extraction import merge_dicts
from src.tools.general_tools import write_to_csv
from src.machine_learning.classification import do_classification
from time import time


def process(total_years):
    """
    :param total_years: dict, required
    :return:
    """
    return merge_dicts(read_csv('data/nba_games_' + total_years + '.csv'), total_years)


if __name__ == "__main__":
    feature_matrix = dict()
    header = list()
    start_time = time()
    print("*** Start feature extraction ***")
    years = ['2002_2003', '2003_2004', '2004_2005', '2005_2006', '2006_2007', '2007_2008', '2008_2009',
             '2009_2010', '2010_2011', '2011_2012', '2012_2013', '2013_2014', '2014_2015', '2015_2016']
    pool = Pool(cpu_count())
    results = pool.map(process, years)
    pool.close()
    for val in results:
        feature_matrix.update(val[0])
        header = val[1]

        print("*** The feature extraction ends after ", time() - start_time, " seconds ***")
    write_to_csv(feature_matrix, header)
    print("*** Start classification ***")
    do_classification(feature_matrix)

