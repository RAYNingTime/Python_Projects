from sklearn.model_selection import GridSearchCV

def hyperparameter_tuning(model, param_grid, X, y):
    grid_search = GridSearchCV(model, param_grid, cv=5)
    grid_search.fit(X, y)
    return grid_search.best_estimator_, grid_search.best_params_
