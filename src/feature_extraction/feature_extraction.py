from src.feature_extraction.simple_stats import simple_stats
from src.feature_extraction.points_features import points_features


def feature_extraction(data_frame):
    """
    :param data_frame: The loaded input file
    :return:
    """
    dict_list = list()
    feature_list = list()

    dict_list.extend(simple_stats(data_frame)[0])
    feature_list.extend(simple_stats(data_frame)[1])
    dict_list.extend(points_features(data_frame)[0])
    feature_list.extend(points_features(data_frame)[1])

    return dict_list, feature_list
