from src.feature_extraction.feature_extraction import feature_extraction


def merge_dicts(data_frame):
    final_dict = dict()
    for d in feature_extraction(data_frame)[0]:
        for key, value in d.iteritems():
            final_dict.setdefault(key, []).append(value)
    return final_dict
