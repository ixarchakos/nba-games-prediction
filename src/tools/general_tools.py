from src.feature_extraction.feature_extraction import feature_extraction
import csv
import numpy as np


def merge_dicts(data_frame):
    final_dict = dict()
    for d in feature_extraction(data_frame)[0]:
        for key, value in d.iteritems():
            final_dict.setdefault(key, []).append(value)
    return final_dict


def write_to_csv(final_dictionary):
    """
    :param final_dictionary:
    :return:
    """
    with open("data/machine_learning/feature_matrix.csv", 'wb') as outfile:
        writer = csv.writer(outfile)
        print final_dictionary.keys()
        print type(final_dictionary.keys())
        writer.writerow(np.array(zip(*[final_dictionary.keys()])).transpose())
        writer.writerows(np.array(zip(*final_dictionary.values())).transpose())


