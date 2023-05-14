def mean_squared_error(y_true, y_pred):
    squared_errors = (y_true - y_pred) ** 2
    mse = squared_errors.mean()
    return mse
