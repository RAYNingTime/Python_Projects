# Code made by Ivan Kosiakov (U214N1534) on 30.03.2023
# Libs to install
# pip install scikit-learn numpy matplotlib

# Libraries
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# Datasets
from sklearn.datasets import load_wine
from sklearn.datasets import load_iris
# Super Bonus Visualization
import matplotlib.pyplot as plt
import numpy as np

# Reading the data set from dataset
data = load_wine()
# data = load_iris()

# Using 70% and the rest, save it for testing
current_test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=current_test_size)

# Setting up a max depth for plot
max_depths = np.arange(1, 31)

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
plt.legend(loc='best')
plt.show()

"""
Results:

Runs = 100
Max_depth = None
Average accuracy: 0.926
Minimal accuracy: 0.889
Maximal accuracy: 0.963

"""

# Note: The code below was used to calculate the results provided earlier.
# Please note that the results may vary if you run the code again due to factors such
# as randomization or changes in the input data. Feel free to uncomment the code and try it out yourself.

"""
# Accuracy is always between 0 and 1
max_accuracy = 0
min_accuracy = 1

amount_of_runs = 100
accuracy_sum = 0
for i in range(amount_of_runs):
    clf_result = DecisionTreeClassifier()
    clf_result.fit(X_train, y_train)

    # Test decision tree classifier and calculate accuracy
    y_result_pred = clf_result.predict(X_test)
    current_accuracy = accuracy_score(y_test, y_result_pred)
    if (current_accuracy <= min_accuracy):
        min_accuracy = current_accuracy

    if (current_accuracy >= max_accuracy):
        max_accuracy = current_accuracy

    accuracy_sum += current_accuracy
accuracy_sum = accuracy_sum / amount_of_runs
print(f"Average accuracy of a {amount_of_runs} of {current_test_size} "
      f"test set with none max_depth is {accuracy_sum:.3f}")
print(f"Minimal accuracy is {min_accuracy:.3f}")
print(f"Maximal accuracy is {max_accuracy:.3f}")
"""
