# courtclusters.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# Load dataset
nba_df = pd.read_csv("Players.csv")

# Select relevant columns and drop rows with missing values
nba_clean = nba_df[['height', 'weight', 'born']].dropna()

# Convert 'born' to 'age'
current_year = 2025
nba_clean['age'] = current_year - nba_clean['born']
nba_clean.drop(columns='born', inplace=True)

# Standardize features
scaler = StandardScaler()
nba_scaled = scaler.fit_transform(nba_clean)

# Optional: Dendrogram (on sample to avoid slowness)
sample_data = nba_scaled[np.random.choice(nba_scaled.shape[0], 200, replace=False)]
linkage_matrix = linkage(sample_data, method='ward')
plt.figure(figsize=(12, 6))
sns.set(style='whitegrid')
dendrogram(linkage_matrix, truncate_mode='lastp', p=20, leaf_rotation=45., leaf_font_size=10.)
plt.title("NBA Players - Dendrogram (Sample of 200)")
plt.xlabel("Cluster Size")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()

# Apply Agglomerative Clustering (3 clusters)
agg_cluster = AgglomerativeClustering(n_clusters=3, linkage='ward')
cluster_labels = agg_cluster.fit_predict(nba_scaled)

# PCA for visualization
pca = PCA(n_components=2)
nba_pca = pca.fit_transform(nba_scaled)
cluster_df = pd.DataFrame(nba_pca, columns=['PC1', 'PC2'])
cluster_df['Cluster'] = cluster_labels

# Scatter plot of clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=cluster_df, x='PC1', y='PC2', hue='Cluster', palette='Set2', s=60)
plt.title("NBA Players Clustered into 3 Groups (PCA Projection)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.legend(title="Cluster")
plt.tight_layout()
plt.show()

# Save final results
nba_result = nba_clean.copy()
nba_result['Cluster'] = cluster_labels
nba_result.to_csv("NBA_Player_Clusters.csv", index=False)