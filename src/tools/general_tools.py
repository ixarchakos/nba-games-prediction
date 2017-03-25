import csv


def write_to_csv(final_dictionary):
    """
    :param final_dictionary:
    :return:
    """
    with open("data/machine_learning/feature_matrix.csv", 'wb') as outfile:
        writer = csv.writer(outfile)
        for k, v in final_dictionary.items():
            l = list()
            l.append(k)
            for v1 in v:
                l.append(v1)
            writer.writerow(l)
