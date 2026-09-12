import numpy as np
import random

class KMeans:
    def __init__(self,n_clusters=2,max_iter=100):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None

    def fit_predict(self,X):
        random_index = random.sample(range(0,X.shape[0]),self.n_clusters)
        # range returns a list from 0 till rows. random sample method takes parameters (list,k) and returns k elements randomly from list
        self.centroids = X[random_index]
        # This is fancy indexing where random index is list of index values, above returns rows of those index values
        for i in range(self.max_iter):
            cluster_grp = self.assign_clusters(X)
            old_centroids = self.centroids
            self.centroids = self.move_centroids(X,cluster_grp)
            if (old_centroids == self.centroids).all(): # .all() is used to ensure conditions is valid when all the centroids match
                break
        return cluster_grp
    
    def assign_clusters(self,X):
        cluster_grp = []
        distances = []

        for row in X:
            for centroid in self.centroids:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))
                # The above is the euclidean distance formula
            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_grp.append(index_pos)
            distances.clear()

        return np.array(cluster_grp)

    def move_centroids(self,X,cluster_grp):
        new_centroids = []
        cluster_type = np.unique(cluster_grp)
        # Since cluster grp contains cluster no. for each row

        for type in cluster_type:
            new_centroids.append(X[cluster_grp == type].mean(axis=0))
            # Here we are finding the mean of the cluster groups one by one

        return np.array(new_centroids)