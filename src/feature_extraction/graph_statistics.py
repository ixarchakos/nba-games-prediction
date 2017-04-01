import networkx as nx
from scipy.sparse.linalg.eigen.arpack.arpack import ArpackError


def graph_statistics(data_frame):
    dict_list = list()
    feature_name_list = list()

    # eigenvector centrality for home and away teams
    centrality = centrality_measures(data_frame)
    dict_list.append(centrality['eigenvector_home'])
    feature_name_list.append("eigenvector_centrality_home")
    dict_list.append(centrality['eigenvector_away'])
    feature_name_list.append("eigenvector_centrality_away")

    dict_list.append(centrality['closeness_home'])
    feature_name_list.append("closeness_centrality_home")
    dict_list.append(centrality['closeness_away'])
    feature_name_list.append("closeness_centrality_away")

    dict_list.append(centrality['shortest_path_home'])
    feature_name_list.append("shortest_path_home")
    dict_list.append(centrality['shortest_path_away'])
    feature_name_list.append("shortest_path_away")

    return dict_list, feature_name_list


def centrality_measures(data_frame):
    centrality_metrics, team_id_dict, eigenvector_home, eigenvector_away, closeness_home, \
        closeness_away, shortest_path_home, shortest_path_away \
        = dict(), dict(), dict(), dict(), dict(), dict(), dict(), dict()
    for index, row in data_frame.iterrows():
        if row['home_team'] not in team_id_dict:
            team_id_dict[row['home_team']] = len(team_id_dict)
        if row['away_team'] not in team_id_dict:
            team_id_dict[row['away_team']] = len(team_id_dict)
        if len(team_id_dict) == 30:
            break
    # create graph and nodes
    g = nx.MultiDiGraph()
    for val in team_id_dict.values():
        g.add_node(val)

    for index, row in data_frame.iterrows():
        home_id = team_id_dict[row['home_team']]
        away_id = team_id_dict[row['away_team']]

        # calculate eigenvector centrality
        try:
            eigenvector_value = nx.eigenvector_centrality_numpy(g, weight='weight')
            closeness_value = nx.closeness_centrality(g, distance='weight', normalized=True)
        except ArpackError:
            eigenvector_home[row["id"]] = 0
            eigenvector_away[row["id"]] = 0
            closeness_home[row["id"]] = 0
            closeness_away[row["id"]] = 0

        eigenvector_home[row["id"]] = eigenvector_value[home_id]
        eigenvector_away[row["id"]] = eigenvector_value[away_id]
        closeness_home[row["id"]] = closeness_value[home_id]
        closeness_away[row["id"]] = closeness_value[away_id]

        # calculate shortest path between the two teams, one for each team
        try:
            shortest_path_home_value = nx.shortest_path_length(g, home_id, away_id, weight='weight')
            shortest_path_home[row["id"]] = shortest_path_home_value
        except nx.NetworkXNoPath:
            shortest_path_home[row["id"]] = -1
        try:
            shortest_path_away_value = nx.shortest_path_length(g, away_id, home_id, weight='weight')
            shortest_path_away[row["id"]] = shortest_path_away_value
        except nx.NetworkXNoPath:
            shortest_path_away[row["id"]] = -1

        # add a new edge
        if row["home_points"] > row["away_points"]:
            difference = row["home_points"] - row["away_points"]
            g.add_weighted_edges_from([(away_id, home_id, difference)])
        else:
            difference = row["away_points"] - row["home_points"]
            g.add_weighted_edges_from([(home_id, away_id, difference)])
    centrality_metrics['eigenvector_home'] = eigenvector_home
    centrality_metrics['eigenvector_away'] = eigenvector_away

    centrality_metrics['closeness_home'] = closeness_home
    centrality_metrics['closeness_away'] = closeness_away

    centrality_metrics['shortest_path_home'] = shortest_path_home
    centrality_metrics['shortest_path_away'] = shortest_path_away

    return centrality_metrics
