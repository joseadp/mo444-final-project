from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier, RandomForestClassifier, AdaBoostClassifier

def get_voting_classifier():
    # Training classifiers
    forest = RandomForestClassifier(n_estimators = 100, n_jobs=3)
    decision_tree = DecisionTreeClassifier(max_depth=15)
    knn = KNeighborsClassifier(n_neighbors=15)
    svm = SVC(gamma=0.0001, C = 100)
    ada = AdaBoostClassifier(n_estimators = 500, learning_rate=0.1)


    return VotingClassifier(estimators=[('rf', forest), ('dt', decision_tree), ('knn', knn), ('svm', svm), ('ada', ada)], voting='hard', weights=[2, 1, 2, 1, 2])

