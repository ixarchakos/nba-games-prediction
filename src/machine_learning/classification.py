from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale
from sknn.mlp import Classifier, Layer
from xgboost.sklearn import XGBClassifier


def do_classification(feature_matrix):
    """
    :param feature_matrix:
    :return:
    """
    type_of_classification = input("1: K-fold classification \n 2: Left-out classification")
    if type_of_classification == 1:
        k_fold_classification()
    elif type_of_classification == 2:
        left_out_classification()
    else:
        print("Wrong type of classification selected!")
        exit(-1)
    return feature_matrix


def left_out_classification():
    return 0


def k_fold_classification():
    return 0


def model_fitting(train_set, train_labels, classifier_name, n_jobs):
    """
    The fitting process with sklearn algorithms.
    :param train_set: numpy array, required
    :param train_labels: list, required
    :param classifier_name: string, required
    :param n_jobs: integer, required
    :return: object
                - Fit classifier model according to the given training data
    """
    classifier_list = {"svm_linear": SVC(probability=True, kernel='linear', C=1.0),
                       "svm_poly": SVC(probability=True, kernel='poly', C=1.0),
                       "svm_rbf": SVC(probability=True, kernel='rbf', C=1.0, gamma=0.01),
                       "linear_svc": LinearSVC(penalty='l2', loss='squared_hinge', dual=True, tol=0.1, C=1.0, multi_class='ovr', fit_intercept=True,
                                               intercept_scaling=1, random_state=None, max_iter=3000),
                       "knn": KNeighborsClassifier(n_neighbors=100, weights='distance', leaf_size=30, n_jobs=n_jobs),
                       "random_forests": RandomForestClassifier(n_estimators=350, criterion='entropy', max_features=12, min_samples_split=2,
                                                                min_samples_leaf=1, max_leaf_nodes=600, n_jobs=n_jobs),
                       "logistic_regression": LogisticRegression(penalty='l2', dual=False, tol=0.0001, C=2.4, fit_intercept=True, intercept_scaling=1,
                                                                 random_state=None, solver='liblinear', max_iter=1000, multi_class='ovr',
                                                                 warm_start=False, n_jobs=n_jobs),
                       "decision_trees": DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2,
                                                                min_samples_leaf=100, min_weight_fraction_leaf=0.0, max_features=None,
                                                                random_state=None, max_leaf_nodes=None, presort=False),
                       "sgd": SGDClassifier(alpha=.0001, n_iter=500, penalty="elasticnet", n_jobs=n_jobs),
                       "neural_network": Classifier(layers=[Layer("Sigmoid", units=14), Layer("Sigmoid", units=13), Layer("Sigmoid", units=12),
                                                            Layer("Sigmoid", units=10), Layer("Softmax")], learning_rate=0.01, n_iter=200,
                                                    batch_size=10, regularize='L1', n_stable=50, dropout_rate=0, verbose=True),
                       "GBC": GradientBoostingClassifier(max_depth=10, max_leaf_nodes=850, min_samples_leaf=15, learning_rate=0.1),
                       "XGB": XGBClassifier(base_score=0.5, colsample_bylevel=1, colsample_bytree=1, gamma=0, learning_rate=0.1, max_delta_step=0,
                                            max_depth=10, min_child_weight=2, missing=None, n_estimators=100, nthread=n_jobs, reg_alpha=0,
                                            objective='binary:logistic', reg_lambda=1, scale_pos_weight=1, seed=0, silent=True, subsample=1)}
    return classifier_list[classifier_name].fit(train_set, train_labels)
