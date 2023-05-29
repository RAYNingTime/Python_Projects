from sklearn.preprocessing import MinMaxScaler

def min_max_scaling(X):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled
