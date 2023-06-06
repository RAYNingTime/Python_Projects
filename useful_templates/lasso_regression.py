from sklearn.linear_model import Lasso

def lasso_regression(X, y, alpha):
    model = Lasso(alpha=alpha)
    model.fit(X, y)
    return model
