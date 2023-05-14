from sklearn.cluster import KMeans

def kmeans_clustering(X, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    return kmeans.labels_, kmeans.cluster_centers_
