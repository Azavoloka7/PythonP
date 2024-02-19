import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data from CSV file
data = pd.read_csv('Cust_Segmentation.csv')

# Display the first few rows of the dataframe to understand its structure
print(data.head())

# Data preprocessing
# Extracting relevant features
X = data[['Age', 'Income', 'DebtIncomeRatio']]  # Update column names to match your dataset

# Normalize the features
from sklearn.preprocessing import StandardScaler
X = np.nan_to_num(X)
X = StandardScaler().fit_transform(X)

# Modeling
# Determine the optimal number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plotting the Elbow Method graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  # Within cluster sum of squares
plt.show()

# From the elbow method, we determine the optimal number of clusters (let's say k=3)
kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_

# Add the cluster labels to the original dataframe
data['Cluster'] = labels

# Visualizing the clusters
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.title('Cluster of customers')
plt.xlabel('Age')
plt.ylabel('Income')
plt.legend()
plt.show()
