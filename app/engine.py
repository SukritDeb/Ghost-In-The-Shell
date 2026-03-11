import numpy as np

class MyDBSCAN:
    def __init__(self, eps=10.0, min_pts=3):
        self.eps = eps
        self.min_pts = min_pts

    def get_dist(self, p1, p2):
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def find_neighbors(self, data, i):
        neighbors = []
        for j in range(len(data)):
            if self.get_dist(data[i], data[j]) < self.eps:
                neighbors.append(j)
        return neighbors

    def fit(self, data):
        labels = [-2] * len(data) 
        cluster_id = 0
        
        print(f"\n--- Starting DBSCAN Analysis (eps={self.eps}, min_pts={self.min_pts}) ---")
        
        for i in range(len(data)):
            if labels[i] != -2:
                continue 

            neighbors = self.find_neighbors(data, i)
            
            if len(neighbors) < self.min_pts:
                labels[i] = -1
                print(f"Point {i}: Neighbors={len(neighbors)} -> [LABEL: NOISE / THREAT]")
            else:
                print(f"Point {i}: Neighbors={len(neighbors)} -> [LABEL: CLUSTER {cluster_id}]")
                self.expand_cluster(data, labels, i, neighbors, cluster_id)
                cluster_id += 1
                
        print("--- Analysis Complete ---\n")
        return labels

    def expand_cluster(self, data, labels, point_idx, neighbors, cluster_id):
        """
        Recursively 'infects' nearby points to grow the cluster.
        """
        labels[point_idx] = cluster_id
        
        i = 0
        while i < len(neighbors):
            neighbor_idx = neighbors[i]
            
            if labels[neighbor_idx] == -1:
                labels[neighbor_idx] = cluster_id
            
            elif labels[neighbor_idx] == -2:
                labels[neighbor_idx] = cluster_id
                
                new_neighbors = self.find_neighbors(data, neighbor_idx)
                if len(new_neighbors) >= self.min_pts:
                    neighbors += new_neighbors
            i += 1