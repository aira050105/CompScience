# Function to calculate Euclidean distance (without math.sqrt)
def euclidean_distance(p1, p2):
    distance_sq = sum((p1[i] - p2[i]) ** 2 for i in range(len(p1)))
    
    # Manual square root using Newton's method
    x = distance_sq
    if x == 0:
        return 0
    approx = x / 2.0
    better_approx = (approx + x / approx) / 2.0
    
    while abs(better_approx - approx) > 1e-6:
        approx = better_approx
        better_approx = (approx + x / approx) / 2.0
    
    return better_approx

# Function to select initial centroids manually (avoiding random.sample)
def initialize_centroids(data, k):
    """Manually select k initial centroids"""
    selected = []
    step = max(1, len(data) // k)  # Pick points at equal intervals
    for i in range(k):
        selected.append(data[i * step % len(data)])
    return selected

# Function to assign points to the nearest centroid
def assign_clusters(data, centroids):
    """Assign each data point to the closest centroid"""
    clusters = {}
    for i in range(len(centroids)):
        clusters[i] = []
    
    for point in data:
        min_dist = float("inf")
        closest_index = -1
        for i in range(len(centroids)):
            dist = euclidean_distance(point, centroids[i])
            if dist < min_dist:
                min_dist = dist
                closest_index = i
        clusters[closest_index].append(point)
    
    return clusters

# Function to update centroids
def update_centroids(clusters):
    """Recalculate centroids as the mean of assigned points"""
    new_centroids = []
    
    for cluster_points in clusters.values():
        if cluster_points:
            new_centroid = []
            for dim in range(len(cluster_points[0])):
                dim_sum = sum(point[dim] for point in cluster_points)
                new_centroid.append(dim_sum / len(cluster_points))
            new_centroids.append(new_centroid)
        else:
            new_centroids.append(cluster_points[0])  # Avoid empty clusters
    
    return new_centroids

# Main K-Means function
def k_means(data, k, max_iterations=100):
    """K-Means Clustering without using any imports"""
    centroids = initialize_centroids(data, k)

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        
        if new_centroids == centroids:  # Stop if centroids don’t change
            break
        
        centroids = new_centroids

    return clusters, centroids

# Example dataset (2D points)
data_points = [
     [1, 2], [2, 3], [3, 3], [6, 7], [7, 8], [8, 9], 
    [10, 11], [12, 13], [13, 14], [15, 16], [16, 17]
]

# Running K-Means with k=2
k = 5
clusters, final_centroids = k_means(data_points, k)

# Printing the results
print("Final Cluster Assignments:")
for cluster_id, points in clusters.items():
    print(f"Cluster {cluster_id + 1}: {points}")

print("\nFinal Centroids:", final_centroids)
