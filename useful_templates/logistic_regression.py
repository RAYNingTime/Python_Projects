from sklearn.linear_model import LogisticRegression

def logistic_regression(X, y):
    model = LogisticRegression()
    model.fit(X, y)
    return model
