import numpy as np

class MyDBSCAN:
    def __init__(self, eps=10.0, min_pts=3):
        """
        eps: The maximum distance between two points to be considered 'neighbors'.
        min_pts: The minimum number of neighbors required to form a 'dense' cluster.
        """
        self.eps = eps
        self.min_pts = min_pts

    def get_dist(self, p1, p2):
        """
        Calculates the Euclidean distance between two points [Size, TimeGap].
        """
        return np.sqrt(np.sum((p1 - p2) ** 2))

    def find_neighbors(self, data, i):
        """
        Scans the dataset and returns a list of indices that are within 'eps' distance of point i.
        """
        neighbors = []
        for j in range(len(data)):
            if self.get_dist(data[i], data[j]) < self.eps:
                neighbors.append(j)
        return neighbors

    def fit(self, data):
        """
        The core DBSCAN algorithm.
        Returns a list of labels: 0+ for clusters, -1 for Noise (Hacker).
        """
        # -2: Unvisited, -1: Noise, 0+: Cluster ID
        labels = [-2] * len(data) 
        cluster_id = 0
        
        print(f"\n--- Starting DBSCAN Analysis (eps={self.eps}, min_pts={self.min_pts}) ---")
        
        for i in range(len(data)):
            if labels[i] != -2:
                continue # Skip points we've already processed
            
            # Step 1: Find neighbors for the current point
            neighbors = self.find_neighbors(data, i)
            
            # Step 2: Check if it's a 'Core Point'
            if len(neighbors) < self.min_pts:
                # Not enough neighbors? Mark as Noise (Potential Anomaly)
                labels[i] = -1
                print(f"Point {i}: Neighbors={len(neighbors)} -> [LABEL: NOISE / THREAT]")
            else:
                # We found a dense area! Start a new cluster
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
            
            # If the neighbor was previously marked as Noise, it's actually a Border Point
            if labels[neighbor_idx] == -1:
                labels[neighbor_idx] = cluster_id
            
            # If the neighbor hasn't been visited yet
            elif labels[neighbor_idx] == -2:
                labels[neighbor_idx] = cluster_id
                
                # Check if this neighbor is also a Core Point
                new_neighbors = self.find_neighbors(data, neighbor_idx)
                if len(new_neighbors) >= self.min_pts:
                    # Add its neighbors to our 'to-process' list (Expanding the crowd)
                    neighbors += new_neighbors
            i += 1