from sklearn.ensemble import GradientBoostingClassifier
from sklearn import metrics
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from src.tools.sampling import k_fold_sample_data_set, random_sample_data_set
from sknn.mlp import Classifier, Layer
from xgboost.sklearn import XGBClassifier
from multiprocessing import cpu_count


def do_classification(feature_matrix, type_of_classification=None, num_of_folds=None):
    """
    :param feature_matrix:
    :param type_of_classification:
    :param num_of_folds:
    :return:
    """
    x = feature_matrix.values[:, 3:]
    y = feature_matrix.values[:, 1]
    if type_of_classification is None:
        type_of_classification = input("1: K-fold classification\n2: Left-out classification\n")
    if type_of_classification == "1":
        if num_of_folds is None:
            num_of_folds = input("Please set the number of folds.\n")
        k_fold_classification(x, y, int(num_of_folds))
    elif type_of_classification == "2":
        left_out_classification(feature_matrix)
    else:
        print("Wrong type of classification selected!")
        exit(-1)
    return feature_matrix


def left_out_classification(feature_matrix):
    """
    :param feature_matrix:
    :return:
    """
    print(feature_matrix)
    return 0


def k_fold_classification(x, y, folds, classifier_name='random_forests', bootstrap=False):
    x_train_list, y_train_list, x_test_list, y_test_list = k_fold_sample_data_set(x, y, folds)
    total_accuracy = 0
    for j in range(0, folds, 1):
        # split data set in train and test set
        if bootstrap:
            x_train, y_train, x_test, y_test = random_sample_data_set(x, y, folds)
        else:
            x_train = x_train_list[j]
            y_train = y_train_list[j]
            x_test = x_test_list[j]
            y_test = y_test_list[j]

        model = model_fitting(x_train, y_train, classifier_name)
        predicted_labels = model.predict(x_test)
        accuracy = metrics.accuracy_score(y_test, predicted_labels)
        total_accuracy += accuracy
        print(accuracy)
    print("Accuracy {0}".format(float(total_accuracy)/float(folds)))


def model_fitting(train_set, train_labels, classifier_name, n_jobs=cpu_count()):
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
                       "random_forests": RandomForestClassifier(n_estimators=350, criterion='entropy', min_samples_split=2,
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
