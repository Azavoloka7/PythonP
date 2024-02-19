import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import scipy.optimize as opt

# Load the dataset
data = pd.read_csv('cell_samples.csv')

# Display the first few rows of the dataset
print(data.head())

# Data preprocessing
# Assuming you might need to preprocess the data if there are missing values or categorical variables to encode.

# For demonstration, let's assume the dataset is clean and doesn't require preprocessing.

# Visualize the data
# For example, let's visualize the distribution of the 'Clump' thickness
plt.hist(data['Clump'], bins=range(1, 11), color='skyblue', edgecolor='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Frequency')
plt.title('Distribution of Clump Thickness')
plt.show()

# Implement a simple analysis or machine learning model
# For example, let's fit a logistic regression model to predict the class (benign or malignant)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Split data into features and target variable
X = data[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
y = data['Class']  # Assuming 'Class' is the target variable

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))
print("Classification Report:\n", classification_report(y_test, predictions))
