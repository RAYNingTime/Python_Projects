# Code made by Ivan Kosiakov (U214N1534) on 30.03.2023

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Dataset
from sklearn.datasets import load_wine
# Super Bonus Visualization
import matplotlib.pyplot as plt
import numpy as np

# Reading the data set
data = load_wine()

# Using 70% and the rest, save it for testing
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

# Setting up a max depth for plot
max_depths = np.arange(1, 21)

# Pre-created arrays to save the result of the calculations
train_scores = []
test_scores = []
for max_depth in max_depths:
    # Setting the max_depth of the Decision Tree for each loop
    clf = DecisionTreeClassifier(max_depth=max_depth)
    clf.fit(X_train, y_train)

    # Prediction of the training set and accuracy calculation
    train_pred = clf.predict(X_train)
    train_accuracy = accuracy_score(y_true=y_train, y_pred=train_pred)

    # Prediction of the test set and accuracy calculation
    test_pred = clf.predict(X_test)
    test_accuracy = accuracy_score(y_true=y_test, y_pred=test_pred)

    # Append scores
    train_scores.append(train_accuracy)
    test_scores.append(test_accuracy)

# Setting up a plot and showing it
plt.plot(max_depths, test_scores, label='Test')
plt.plot(max_depths, train_scores, label='Train')
plt.ylabel('Accuracy Score')
plt.xlabel('Maximum Depth')
plt.legend(loc='upper left')
plt.show()
