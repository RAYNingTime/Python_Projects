from sklearn.decomposition import PCA

def pca(X, n_components):
    pca = PCA(n_components=n_components)
    pca.fit(X)
    X_transformed = pca.transform(X)
    return X_transformed
