import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from kmeans import KMeans

# Generate synthetic data
centroids = [(-5, 5), (5, 5),(-2.5,-2.5)]
cluster_std = [1, 1,1]
X, y = make_blobs(n_samples=100, centers=centroids, cluster_std=cluster_std, random_state=42, n_features=2)

# Create a KMeans instance
km= KMeans(n_clusters=3, max_iter=100)

y_means=km.fit_predict(X)

plt.scatter(X[y_means == 0, 0], X[y_means == 0, 1], s=50, c='red', label='Cluster 1')
plt.scatter(X[y_means == 1, 0], X[y_means == 1, 1], s=50, c='blue', label='Cluster 2')
plt.scatter(X[y_means == 2, 0], X[y_means == 2, 1], s=50, c='green', label='Cluster 3')
plt.legend()
plt.show()