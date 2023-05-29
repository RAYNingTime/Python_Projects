from sklearn.ensemble import GradientBoostingClassifier

def gradient_boosting(X, y):
    model = GradientBoostingClassifier()
    model.fit(X, y)
    return model
