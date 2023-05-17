from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def select_features(X, y, k=10):
    selector = SelectKBest(score_func=chi2, k=k)
    X_new = selector.fit_transform(X, y)
    return X_new
