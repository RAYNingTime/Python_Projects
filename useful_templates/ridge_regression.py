from sklearn.linear_model import Ridge

def ridge_regression(X, y, alpha):
    model = Ridge(alpha=alpha)
    model.fit(X, y)
    return model
