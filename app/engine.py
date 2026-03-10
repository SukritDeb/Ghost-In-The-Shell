import numpy as np

class MyDBSCAN:
    def __init__(self, eps=10.0, min_pts=3):
        self.eps = eps
        self.min_pts = min_pts

    def get_dist(self, p1, p2):
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def find_neighbors(self, data, i):
        return [j for j in range(len(data)) if self.get_dist(data[i], data[j]) < self.eps]

    def fit(self, data):
        labels = [-2] * len(data) # -2 = Unvisited, -1 = Noise
        cluster_id = 0
        for i in range(len(data)):
            if labels[i] != -2: continue
            neighbors = self.find_neighbors(data, i)
            if len(neighbors) < self.min_pts:
                labels[i] = -1
            else:
                labels[i] = cluster_id
                self.expand(data, labels, neighbors, cluster_id)
                cluster_id += 1
        return labels

    def expand(self, data, labels, neighbors, cluster_id):
        i = 0
        while i < len(neighbors):
            idx = neighbors[i]
            if labels[idx] == -1: labels[idx] = cluster_id
            elif labels[idx] == -2:
                labels[idx] = cluster_id
                new_neighbors = self.find_neighbors(data, idx)
                if len(new_neighbors) >= self.min_pts:
                    neighbors += new_neighbors
            i += 1