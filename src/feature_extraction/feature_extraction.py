from src.feature_extraction.simple_stats import simple_stats
from src.feature_extraction.points_features import points_features
from src.feature_extraction.non_points_features import non_points_features
from src.feature_extraction.advanced_statistics import advanced_statistics


def feature_extraction(data_frame, total_years):
    """
    :param data_frame: The loaded input file
    :param total_years:
    :return:
    """
    dict_list = list()
    feature_list = list()

    dict_list.extend(simple_stats(data_frame, total_years)[0])
    feature_list.extend(simple_stats(data_frame, total_years)[1])
    dict_list.extend(points_features(data_frame)[0])
    feature_list.extend(points_features(data_frame)[1])
    dict_list.extend(non_points_features(data_frame)[0])
    feature_list.extend(non_points_features(data_frame)[1])
    dict_list.extend(advanced_statistics(data_frame)[0])
    feature_list.extend(advanced_statistics(data_frame)[1])
    return dict_list, feature_list


def merge_dicts(data_frame, total_years):
    final_dict = dict()
    extraction = feature_extraction(data_frame, total_years)
    for d in extraction[0]:
        for key, value in d.iteritems():
            final_dict.setdefault(key, []).append(value)
    return final_dict, extraction[1]
